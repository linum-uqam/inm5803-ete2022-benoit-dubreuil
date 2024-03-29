import pathlib

import imageio
import numpy as np
import numpy.typing as npt


# TODO : Specialize PSF NDArray type
# TODO : Migrate imageio v2 API to v3 API :
#  See https://imageio.readthedocs.io/en/stable/reference/userapi.html#migrating-to-the-v3-api
# TODO : Load PSF 3D
def load_psf(filename: pathlib.Path) -> npt.NDArray:
    """Load a Point-Spread Function (PSF) from a file.

    Parameters
    ----------
    filename
        Input volume filename. Must be a volume format supported by `imageio.volwrite`. Example : `.tif` and `.tiff`.

    Note
    ----
    Only the middle slice along the first dimension will be used
    .. code-block:: python
        psf = psf[int(psf.shape[0]/2), ...]

    """
    psf: npt.NDArray = imageio.volread(filename)
    psf = np.squeeze(psf)

    psf_2d = psf[int(psf.shape[0] / 2), ...]
    psf_2d = np.squeeze(psf_2d)
    psf_2d = psf_2d / psf_2d.sum()

    return psf_2d
