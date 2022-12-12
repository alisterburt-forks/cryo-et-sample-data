"""Immature HIV-1 virus-like particle data from EMPIAR-10164.

This dataset contains a tomogram reconstructed from images in EMPIAR-10164.
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

import mrcfile

from cryo_et_sample_data._data_set import DataSet

if TYPE_CHECKING:
    from napari.types import LayerDataTuple

hiv_config = {
    "name": "hiv",
    "author": "Alister Burt",
    "description": __doc__,
    "base_url": "doi:10.5281/zenodo.6504891/",
    "tomogram_metadata": {
        "file_name": "01_10.00Apx.mrc",
        "checksum": "md5:426325d006fe04276ea01df9d83ad510",
        "reader": mrcfile.read,
    },
}

hiv = DataSet.from_dict(hiv_config)
