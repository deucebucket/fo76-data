import bpy
import os
import math

WORK = '/var/home/deucebucket/ai-drive/fo76-data/blender_work'
OUT = '/var/home/deucebucket/ai-drive/fo76-data/blender_work'

# Clear scene
bpy.ops.wm.read_factory_settings(use_empty=True)

# Import OBJ
bpy.ops.wm.obj_import(filepath=os.path.join(WORK, 'gutpuker_mesh.obj'))

imported = [o for o in bpy.context.scene.objects if o.type == 'MESH']
print(f"Imported {len(imported)} mesh objects")
for obj in imported:
    print(f"  {obj.name}: {len(obj.data.vertices)} verts")

# Join all meshes
if len(imported) > 1:
    bpy.context.view_layer.objects.active = imported[0]
    for obj in imported:
        obj.select_set(True)
    bpy.ops.object.join()

model = bpy.context.active_object or [o for o in bpy.context.scene.objects if o.type == 'MESH'][0]
bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME')

dims = model.dimensions
max_dim = max(dims)
print(f"Dimensions: {dims[0]:.2f} x {dims[1]:.2f} x {dims[2]:.2f}")

# Apply textures
tex_dir = os.path.join(WORK, 'textures/actors/gutpuker/')
for slot in model.material_slots:
    mat = slot.material
    if not mat:
        continue
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    bsdf = nodes.get('Principled BSDF')
    if not bsdf:
        continue
    mat_name = mat.name.lower()
    for part in ['body', 'arm', 'tentacle']:
        if part in mat_name:
            tex_file = os.path.join(tex_dir, f'gutpuker_{part}_d.dds')
            if os.path.exists(tex_file):
                tex_node = nodes.new('ShaderNodeTexImage')
                try:
                    tex_node.image = bpy.data.images.load(tex_file)
                    mat.node_tree.links.new(tex_node.outputs['Color'], bsdf.inputs['Base Color'])
                    print(f"Texture: {part} -> {mat.name}")
                except Exception as e:
                    print(f"Texture failed: {e}")
            break

# Dark background
world = bpy.data.worlds.new('World')
bpy.context.scene.world = world
world.use_nodes = True
bg = world.node_tree.nodes['Background']
bg.inputs['Color'].default_value = (0.015, 0.015, 0.015, 1)

# 3-point lighting
def add_sun(name, energy, rx, rz):
    data = bpy.data.lights.new(name, 'SUN')
    data.energy = energy
    obj = bpy.data.objects.new(name, data)
    bpy.context.scene.collection.objects.link(obj)
    obj.rotation_euler = (math.radians(rx), 0, math.radians(rz))

add_sun('Key', 4.0, 50, 40)
add_sun('Fill', 1.5, 65, -55)
add_sun('Rim', 2.5, 25, 175)

# Camera
cam_data = bpy.data.cameras.new('Camera')
cam_obj = bpy.data.objects.new('Camera', cam_data)
bpy.context.scene.collection.objects.link(cam_obj)
bpy.context.scene.camera = cam_obj
cam_data.lens = 85

# Render settings
scene = bpy.context.scene
scene.render.engine = 'CYCLES'
scene.cycles.device = 'GPU'

prefs = bpy.context.preferences.addons.get('cycles')
if prefs:
    cprefs = prefs.preferences
    cprefs.compute_device_type = 'CUDA'
    cprefs.get_devices()
    for d in cprefs.devices:
        d.use = True
        print(f"GPU: {d.name} ({d.type})")

scene.cycles.samples = 128
scene.render.resolution_x = 1024
scene.render.resolution_y = 1400
scene.render.film_transparent = False
scene.render.image_settings.file_format = 'PNG'

# Compute real bounding box center
import mathutils
bb = [model.matrix_world @ mathutils.Vector(c) for c in model.bound_box]
xs = [v.x for v in bb]
ys = [v.y for v in bb]
zs = [v.z for v in bb]
center = mathutils.Vector(((min(xs)+max(xs))/2, (min(ys)+max(ys))/2, (min(zs)+max(zs))/2))
extent = max(max(xs)-min(xs), max(ys)-min(ys), max(zs)-min(zs))
print(f"BBox center: {center}, extent: {extent:.1f}")

def set_camera(dist_mult, height_mult, angle_deg):
    angle = math.radians(angle_deg)
    dist = extent * dist_mult
    cam_obj.location = (
        center.x + dist * math.sin(angle),
        center.y - dist * math.cos(angle),
        center.z + extent * height_mult
    )
    direction = center - cam_obj.location
    rot_quat = direction.to_track_quat('-Z', 'Y')
    cam_obj.rotation_euler = rot_quat.to_euler()

views = [
    ('front', 1.8, 0.15, 15),
    ('front_34', 1.8, 0.15, 35),
    ('side', 1.8, 0.15, 90),
    ('back', 1.8, 0.15, 195),
    ('low_angle', 1.5, -0.3, 20),
    ('other_side', 1.8, 0.15, -80),
]

for name, dist, height, angle in views:
    set_camera(dist, height, angle)
    scene.render.filepath = os.path.join(OUT, f'gutpuker_{name}.png')
    bpy.ops.render.render(write_still=True)
    print(f"Rendered: {name}")

# Head closeup
cam_data.lens = 135
set_camera(1.0, 0.6, 10)
target = center.copy()
target.z += extent * 0.4
direction = target - cam_obj.location
rot_quat = direction.to_track_quat('-Z', 'Y')
cam_obj.rotation_euler = rot_quat.to_euler()
scene.render.resolution_x = 1024
scene.render.resolution_y = 1024
scene.render.filepath = os.path.join(OUT, 'gutpuker_head.png')
bpy.ops.render.render(write_still=True)
print("Rendered: head closeup")

print("ALL RENDERS COMPLETE")
