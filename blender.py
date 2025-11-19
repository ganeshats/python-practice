###############################################
# ADVANCED HOME TEMPLATE — COLOR CYCLING
# Code from chatgpt to use in blender
# run using 'blender --background --python home_color_cycle.py' Command
###############################################

import bpy
from mathutils import Vector
import math
import os

#######################################
# CLEAN SCENE
#######################################
def clean_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

clean_scene()

#######################################
# PARAMETERS
#######################################
params = {
    "wall_height": 3.0,
    "wall_thickness": 0.2,
    "house_length": 10.0,
    "house_width": 8.0,

    # Render config
    "fps": 24,
    "duration": 6,  # seconds
}

#######################################
# COLOR PALETTES (ADD AS MANY AS YOU WANT)
#######################################
color_palettes = {
    "Minimal_White": {
        "floor": (0.25, 0.25, 0.25, 1),
        "walls": (0.95, 0.95, 0.95, 1),
        "ceiling": (1.0, 1.0, 1.0, 1)
    },
    "Warm_Wood": {
        "floor": (0.35, 0.20, 0.10, 1),
        "walls": (0.92, 0.85, 0.75, 1),
        "ceiling": (1.0, 0.98, 0.95, 1)
    },
    "Cool_Gray": {
        "floor": (0.2, 0.2, 0.25, 1),
        "walls": (0.7, 0.7, 0.75, 1),
        "ceiling": (0.9, 0.9, 0.95, 1)
    },
    "Dark_Mode": {
        "floor": (0.05, 0.05, 0.05, 1),
        "walls": (0.2, 0.2, 0.22, 1),
        "ceiling": (0.3, 0.3, 0.35, 1)
    },
}

#######################################
# MATERIAL CREATION
#######################################
def make_material(name):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    return mat

floor_mat = make_material("FloorMat")
walls_mat = make_material("WallsMat")
ceil_mat  = make_material("CeilingMat")

def apply_colors(palette):
    floor_mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = palette["floor"]
    walls_mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = palette["walls"]
    ceil_mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value  = palette["ceiling"]

#######################################
# CREATE FLOOR & CEILING
#######################################
def create_floor_ceiling():
    l = params["house_length"]
    w = params["house_width"]

    # Floor
    bpy.ops.mesh.primitive_plane_add()
    floor = bpy.context.active_object
    floor.scale = (l/2, w/2, 1)
    floor.data.materials.append(floor_mat)

    # Ceiling
    bpy.ops.mesh.primitive_plane_add(location=(0, 0, params["wall_height"]))
    ceiling = bpy.context.active_object
    ceiling.scale = (l/2, w/2, 1)
    ceiling.data.materials.append(ceil_mat)

create_floor_ceiling()

#######################################
# CREATE WALLS (PARAMETRIC)
#######################################
def create_wall(length, thickness, height, pos, rot=0):
    bpy.ops.mesh.primitive_cube_add(size=1, location=pos)
    wall = bpy.context.active_object
    wall.scale = (length/2, thickness/2, height/2)
    wall.rotation_euler[2] = rot
    wall.data.materials.append(walls_mat)
    return wall

l = params["house_length"]
w = params["house_width"]
t = params["wall_thickness"]
h = params["wall_height"]

# 4 walls
create_wall(l, t, h, (0,  w/2, h/2))
create_wall(l, t, h, (0, -w/2, h/2))
create_wall(w, t, h, ( l/2, 0, h/2), rot=math.pi/2)
create_wall(w, t, h, (-l/2, 0, h/2), rot=math.pi/2)

#######################################
# LIGHTING
#######################################
def setup_lighting():
    bpy.ops.object.light_add(type="SUN", location=(4, -4, 6))
    sun = bpy.context.active_object
    sun.data.energy = 3
    sun.rotation_euler = (math.radians(60), 0, math.radians(45))

setup_lighting()

#######################################
# CAMERA PATH (BEZIER WALKTHROUGH)
#######################################
def setup_camera_path():
    fps = params["fps"]
    duration = params["duration"]
    total_frames = fps * duration
    scene = bpy.context.scene

    # Camera
    bpy.ops.object.camera_add(location=(0, -5, 1.7))
    cam = bpy.context.active_object
    scene.camera = cam

    # Path
    bpy.ops.curve.primitive_bezier_curve_add()
    path = bpy.context.active_object
    path.name = "CameraPath"

    spline = path.data.splines[0]
    spline.bezier_points[0].co = Vector((0, -5, 1.7))
    spline.bezier_points[1].co = Vector((0,  5, 1.7))

    # Follow path
    follow = cam.constraints.new('FOLLOW_PATH')
    follow.target = path
    follow.use_curve_follow = True

    follow.offset_factor = 0
    follow.keyframe_insert("offset_factor", frame=1)
    follow.offset_factor = 1
    follow.keyframe_insert("offset_factor", frame=total_frames)

    scene.frame_start = 1
    scene.frame_end = total_frames

setup_camera_path()

#######################################
# RENDER SETUP
#######################################
def setup_render(out_path):
    scene = bpy.context.scene
    scene.render.engine = "CYCLES"
    scene.cycles.samples = 64
    scene.render.resolution_x = 1920
    scene.render.resolution_y = 1080
    scene.render.image_settings.file_format = "FFMPEG"
    scene.render.ffmpeg.format = "MPEG4"
    scene.render.ffmpeg.codec = "H264"
    scene.render.filepath = out_path

#######################################
# MAIN COLOR LOOP
#######################################
output_dir = "//renders/"
if not os.path.exists(bpy.path.abspath(output_dir)):
    os.makedirs(bpy.path.abspath(output_dir))

for name, palette in color_palettes.items():
    print(f"\n=== Rendering Palette: {name} ===")
    apply_colors(palette)
    setup_render(f"{output_dir}{name}.mp4")
    bpy.ops.render.render(animation=True)

print("\nALL RENDERS COMPLETE!")
