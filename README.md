## Pixel Manipulation

The **Pixel Manipulation** module provides basic image processing and steganography tools.

### Features
- Read and modify pixel values (RGB)
- Apply basic filters:
  - Grayscale
  - Invert colors
  - Threshold (binary)
- Embed and extract hidden messages in images (LSB steganography)
- Export modified images in common formats

### Example
```python
from tools.pixel_tool import invert_image, hide_message, extract_message

