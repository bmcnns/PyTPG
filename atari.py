import numpy as np
import random
from typing import Tuple

class Atari:
	NTSC_PALETTE = np.array([
		0x000000,0x000000,0x4a4a4a,0x4a4a4a,0x6f6f6f,0x6f6f6f,0x8e8e8e,0x8e8e8e,
		0xaaaaaa,0xaaaaaa,0xc0c0c0,0xc0c0c0,0xd6d6d6,0xd6d6d6,0xececec,0xececec,
		0x484800,0x404040,0x69690f,0x5f5f5f,0x86861d,0x7a7a7a,0xa2a22a,0x949494,
		0xbbbb35,0xacacac,0xd2d240,0xc1c1c1,0xe8e84a,0xd6d6d6,0xfcfc54,0xe9e9e9,
		0x7c2c00,0x3f3f3f,0x904811,0x575757,0xa26221,0x6e6e6e,0xb47a30,0x838383,
		0xc3903d,0x969696,0xd2a44a,0xa7a7a7,0xdfb755,0xb8b8b8,0xecc860,0xc7c7c7,
		0x901c00,0x3b3b3b,0xa33915,0x555555,0xb55328,0x6b6b6b,0xc66c3a,0x818181,
		0xd5824a,0x949494,0xe39759,0xa7a7a7,0xf0aa67,0xb7b7b7,0xfcbc74,0xc7c7c7,
		0x940000,0x2c2c2c,0xa71a1a,0x444444,0xb83232,0x5a5a5a,0xc84848,0x6e6e6e,
		0xd65c5c,0x808080,0xe46f6f,0x929292,0xf08080,0xa1a1a1,0xfc9090,0xb0b0b0,
		0x840064,0x333333,0x97197a,0x4a4a4a,0xa8308f,0x5f5f5f,0xb846a2,0x737373,
		0xc659b3,0x848484,0xd46cc3,0x959595,0xe07cd2,0xa4a4a4,0xec8ce0,0xb2b2b2,
		0x500084,0x272727,0x68199a,0x3f3f3f,0x7d30ad,0x555555,0x9246c0,0x6b6b6b,
		0xa459d0,0x7d7d7d,0xb56ce0,0x8f8f8f,0xc57cee,0x9f9f9f,0xd48cfc,0xaeaeae,
		0x140090,0x161616,0x331aa3,0x313131,0x4e32b5,0x494949,0x6848c6,0x606060,
		0x7f5cd5,0x747474,0x956fe3,0x888888,0xa980f0,0x999999,0xbc90fc,0xa9a9a9,
		0x000094,0x111111,0x181aa7,0x292929,0x2d32b8,0x404040,0x4248c8,0x555555,
		0x545cd6,0x686868,0x656fe4,0x797979,0x7580f0,0x898989,0x8490fc,0x999999,
		0x001c88,0x202020,0x183b9d,0x3c3c3c,0x2d57b0,0x555555,0x4272c2,0x6d6d6d,
		0x548ad2,0x828282,0x65a0e1,0x969696,0x75b5ef,0xa8a8a8,0x84c8fc,0xbababa,
		0x003064,0x282828,0x185080,0x454545,0x2d6d98,0x5f5f5f,0x4288b0,0x787878,
		0x54a0c5,0x8d8d8d,0x65b7d9,0xa2a2a2,0x75cceb,0xb6b6b6,0x84e0fc,0xc8c8c8,
		0x004030,0x2b2b2b,0x18624e,0x4a4a4a,0x2d8169,0x656565,0x429e82,0x7f7f7f,
		0x54b899,0x979797,0x65d1ae,0xadadad,0x75e7c2,0xc1c1c1,0x84fcd4,0xd4d4d4,
		0x004400,0x282828,0x1a661a,0x474747,0x328432,0x626262,0x48a048,0x7c7c7c,
		0x5cba5c,0x939393,0x6fd26f,0xa9a9a9,0x80e880,0xbdbdbd,0x90fc90,0xcfcfcf,
		0x143c00,0x292929,0x355f18,0x4a4a4a,0x527e2d,0x686868,0x6e9c42,0x848484,
		0x87b754,0x9d9d9d,0x9ed065,0xb5b5b5,0xb4e775,0xcbcbcb,0xc8fc84,0xdfdfdf,
		0x303800,0x2f2f2f,0x505916,0x4f4f4f,0x6d762b,0x6b6b6b,0x88923e,0x858585,
		0xa0ab4f,0x9d9d9d,0xb7c25f,0xb3b3b3,0xccd86e,0xc8c8c8,0xe0ec7c,0xdcdcdc,
		0x482c00,0x2f2f2f,0x694d14,0x4f4f4f,0x866a26,0x6b6b6b,0xa28638,0x858585,
		0xbb9f47,0x9d9d9d,0xd2b656,0xb3b3b3,0xe8cc63,0xc8c8c8,0xfce070,0xdcdcdc
	]);
	"""
	The NTSC colour palette used by the STELLA Atari emulator

	:meta hide-value:
	"""

	SECAM_PALETTE = np.array([
		0x000000,0x000000,0x2121ff,0x3a3a3a,0xf03c79,0x797979,0xff50ff,0x989898,
		0x7fff00,0xbcbcbc,0x7fffff,0xd9d9d9,0xffff3f,0xe9e9e9,0xffffff,0xffffff,
		0x000000,0x000000,0x2121ff,0x3a3a3a,0xf03c79,0x797979,0xff50ff,0x989898,
		0x7fff00,0xbcbcbc,0x7fffff,0xd9d9d9,0xffff3f,0xe9e9e9,0xffffff,0xffffff,
		0x000000,0x000000,0x2121ff,0x3a3a3a,0xf03c79,0x797979,0xff50ff,0x989898,
		0x7fff00,0xbcbcbc,0x7fffff,0xd9d9d9,0xffff3f,0xe9e9e9,0xffffff,0xffffff,
		0x000000,0x000000,0x2121ff,0x3a3a3a,0xf03c79,0x797979,0xff50ff,0x989898,
		0x7fff00,0xbcbcbc,0x7fffff,0xd9d9d9,0xffff3f,0xe9e9e9,0xffffff,0xffffff,
		0x000000,0x000000,0x2121ff,0x3a3a3a,0xf03c79,0x797979,0xff50ff,0x989898,
		0x7fff00,0xbcbcbc,0x7fffff,0xd9d9d9,0xffff3f,0xe9e9e9,0xffffff,0xffffff,
		0x000000,0x000000,0x2121ff,0x3a3a3a,0xf03c79,0x797979,0xff50ff,0x989898,
		0x7fff00,0xbcbcbc,0x7fffff,0xd9d9d9,0xffff3f,0xe9e9e9,0xffffff,0xffffff,
		0x000000,0x000000,0x2121ff,0x3a3a3a,0xf03c79,0x797979,0xff50ff,0x989898,
		0x7fff00,0xbcbcbc,0x7fffff,0xd9d9d9,0xffff3f,0xe9e9e9,0xffffff,0xffffff,
		0x000000,0x000000,0x2121ff,0x3a3a3a,0xf03c79,0x797979,0xff50ff,0x989898,
		0x7fff00,0xbcbcbc,0x7fffff,0xd9d9d9,0xffff3f,0xe9e9e9,0xffffff,0xffffff,
		0x000000,0x000000,0x2121ff,0x3a3a3a,0xf03c79,0x797979,0xff50ff,0x989898,
		0x7fff00,0xbcbcbc,0x7fffff,0xd9d9d9,0xffff3f,0xe9e9e9,0xffffff,0xffffff,
		0x000000,0x000000,0x2121ff,0x3a3a3a,0xf03c79,0x797979,0xff50ff,0x989898,
		0x7fff00,0xbcbcbc,0x7fffff,0xd9d9d9,0xffff3f,0xe9e9e9,0xffffff,0xffffff,
		0x000000,0x000000,0x2121ff,0x3a3a3a,0xf03c79,0x797979,0xff50ff,0x989898,
		0x7fff00,0xbcbcbc,0x7fffff,0xd9d9d9,0xffff3f,0xe9e9e9,0xffffff,0xffffff,
		0x000000,0x000000,0x2121ff,0x3a3a3a,0xf03c79,0x797979,0xff50ff,0x989898,
		0x7fff00,0xbcbcbc,0x7fffff,0xd9d9d9,0xffff3f,0xe9e9e9,0xffffff,0xffffff,
		0x000000,0x000000,0x2121ff,0x3a3a3a,0xf03c79,0x797979,0xff50ff,0x989898,
		0x7fff00,0xbcbcbc,0x7fffff,0xd9d9d9,0xffff3f,0xe9e9e9,0xffffff,0xffffff,
		0x000000,0x000000,0x2121ff,0x3a3a3a,0xf03c79,0x797979,0xff50ff,0x989898,
		0x7fff00,0xbcbcbc,0x7fffff,0xd9d9d9,0xffff3f,0xe9e9e9,0xffffff,0xffffff,
		0x000000,0x000000,0x2121ff,0x3a3a3a,0xf03c79,0x797979,0xff50ff,0x989898,
		0x7fff00,0xbcbcbc,0x7fffff,0xd9d9d9,0xffff3f,0xe9e9e9,0xffffff,0xffffff,
		0x000000,0x000000,0x2121ff,0x3a3a3a,0xf03c79,0x797979,0xff50ff,0x989898,
		0x7fff00,0xbcbcbc,0x7fffff,0xd9d9d9,0xffff3f,0xe9e9e9,0xffffff,0xffffff
	]);
	"""
	The SECAM colour palette used by the STELLA Atari emulator

	:meta hide-value:
	"""

	SECAM_RGB_MAPPING = {
		0x000000: (0, 0, 0),
		0x2121ff: (33, 33, 255),
		0x3a3a3a: (58, 58, 58),
		0xf03c79: (240, 60, 121),
		0x797979: (121, 121, 121),
		0xff50ff: (255, 80, 255),
		0x989898: (152, 152, 152),
		0x7fff00: (127, 255, 0),
		0xbcbcbc: (188, 188, 188),
		0x7fffff: (127, 255, 255),
		0xd9d9d9: (217, 217, 217),
		0xffff3f: (255, 255, 63),
		0xe9e9e9: (233, 233, 233),
		0xffffff: (255, 255, 255)
	}
	"""
	Maps SECAM bytes to RGB values (3,) 

	:meta hide-value:
	"""

	SECAM_BYTE_ENCODING = {
		0x000000: 0b00000000,
		0x2121ff: 0b00000001,
		0x3a3a3a: 0b00000010,
		0xf03c79: 0b00000011,
		0x797979: 0b00000100, 
		0xff50ff: 0b00000101, 
		0x989898: 0b00000110,
		0x7fff00: 0b00000111,
		0xbcbcbc: 0b00001000,  
		0x7fffff: 0b00001001, 
		0xd9d9d9: 0b00001010, 
		0xffff3f: 0b00001011, 
		0xe9e9e9: 0b00001100, 
		0xffffff: 0b00001101 
	}
	"""
	Byte encodings of SECAM colours 

	:meta hide-value:
	"""

	NTSC_SECAM_MAPPING = dict(zip(NTSC_PALETTE, SECAM_PALETTE))
	"""
	Mapping between NTSC colours to SECAM colours

	:meta hide-value:
	"""

	@staticmethod
	def RGBtoSECAM(buffer: np.ndarray) -> np.ndarray:
		"""
		Converts a (210,160,3) screen buffer to a (210,160) buffer of SECAM colour-encoded bytes.

		:param buffer: the (210,160,3) screen of RGB pixels

		:return: a (210,160) buffer of SECAM colour-encoded bytes.
		"""
		
		r,g,b = buffer[:,:,0], buffer[:, :, 1], buffer[:, :, 2]
		ntsc = (r * 65536) + (g * 256) + b
		return np.vectorize(Atari.NTSC_SECAM_MAPPING.get)(ntsc)
	
	@staticmethod
	def SECAMtoRGB(buffer: np.ndarray) -> np.ndarray:
		"""
		Converts a (210,160) buffer of SECAM colour-encoded bytes to a (210,160,3) RGB image.

		:param buffer: the (210, 160) buffer of SECAM colour-encoded bytes

		:return: a (210,160,3) RGB image.
		"""
		rgb_colors = np.array([SECAM_RGB_MAPPING[color] for color in buffer.flat], dtype=np.uint8)
		return rgb_colors.reshape(buffer.shape + (3,))

	@staticmethod
	def checkerMask(buffer: np.ndarray) -> np.ndarray:
		"""
		Applies a checkerboard mask to mask-out every other pixel in a buffer.
		This is used to reduce the amount of pixel information.
		This works because all important game entities are larger than a single pixel.

		:param buffer: a (210,160) SECAM byte encoded image.

		:return: a (210,160) SECAM byte encoded image with half the pixels masked to black.
		"""
		# Create a checkerboard mask
		mask = np.indices(buffer.shape).sum(axis=0) % 2 == 0

		# Create a copy of the buffer
		result = buffer.copy()

		# Set the skipped pixels to 0x0
		result[~mask] = 0x0

		return result

	@staticmethod
	def reduceDimensionality(buffer: np.ndarray, dimensions: Tuple[int] = (42,32)) -> np.ndarray:
		"""
		Downsamples a (210,160) image into a (42,32) image and returns a (1344,) feature vector.
		This operation is performed by splitting the image into 'chunkSize' non-overlapping chunks.
		Each non-overlapping chunk is a 5x5 image representing one pixel in the (42,32) image.
		The pixel in the (42,32) image is a colour uniformly sampled from the non-black colours within the chunk.
		The (42,32) image is flattened into a (1344,) feature vector.

		:param buffer: a (210,160) SECAM byte-encoded image
		:param dimensions: the shape of the downsampled image. recommended: (42,32).
		
		:return: 
		"""
		result = np.zeros(shape=dimensions)
		chunkSize = 5

		# Break the 210, 160 image into chunks of chunkSize (5)
		for j in range(0, dimensions[0]):
			for i in range(0, dimensions[1]):
				row = j * chunkSize
				col = i * chunkSize
				chunk = buffer[row:row+chunkSize, col:col+chunkSize]

				# Filter out all the black or masked pixels
				colours = chunk[chunk != 0]

				# Uniformly sample a non-black/masked pixel
				if len(colours) != 0:
					result[j][i] = random.choice(colours)
					# All pixels are black, therefore the sampled pixel must be black
				else:
					result[j][i] = 0

		# Convert the (42,32) SECAM-encoded image to a 1344-dim state vector
		# where each feature ranges from 0 to 13
		return np.array([Atari.SECAM_BYTE_ENCODING[color] for color in result.flat])

	@staticmethod
	def preprocess(buffer: np.ndarray) -> np.ndarray:
		"""
		Apply this method to reduce the dimensionality of the Atari's screen from (210,160,3) to a (1344,) feature vector.

		:param buffer: The Atari screen's raw RGB data of shape (210,160,3).
		:return: The Atari screen downsampled to a feature vector of shape (1344,)
		"""
		return Atari.reduceDimensionality(Atari.checkerMask(Atari.RGBtoSECAM(buffer)))
