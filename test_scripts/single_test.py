import openslide
from pathlib import Path

slide_path = "/home/jaywardhan/Documents/samyak_CRC/wsi/064f3779-aeb1-4be1-9b86-76edc95a5c28/TCGA-D5-6535-01Z-00-DX1.0d7485ff-cf98-4c86-8a61-c7364f41b8b0.svs"
slide = openslide.OpenSlide(slide_path)

print("Dimensions (level 0):", slide.dimensions)
print("Level count:", slide.level_count)
print("Level dimensions:", slide.level_dimensions)
print("Level downsamples:", slide.level_downsamples)
print("MPP-x:", slide.properties.get("openslide.mpp-x", "NOT FOUND"))
print("MPP-y:", slide.properties.get("openslide.mpp-y", "NOT FOUND"))
print("Objective power:", slide.properties.get(
    "openslide.objective-power", "NOT FOUND"))
