# Mocap Converter

**Mocap Converter** is a simple Python application for converting C3D motion capture files into FBX format. It’s designed to streamline the motion data pipeline for use in environments like Unity or Blender.

---

## Features

- GUI interface built with `tkinter`
- Reads `.c3d` files using `ezc3d`
- (Planned) Exports `.fbx` via FBX SDK or Blender

---

## Requirements

- Python 3.10+
- [ezc3d](https://github.com/pyomeca/ezc3d)
- (Planned) Autodesk FBX SDK or Blender for exporting

Install dependencies:

```bash
poetry install
