# Copyright 2019-2025 The kikuchipy developers
#
# This file is part of kikuchipy.
#
# kikuchipy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# kikuchipy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with kikuchipy. If not, see <http://www.gnu.org/licenses/>.

"""Running this file will pre-cache all datasets downloaded by the
python package pooch, and verify supported but unneeded files are
still reachable on Zenodo.

This was implimented to circumvent the API limitations on Zenodo
discussed in the following blog post.
https://blog.zenodo.org/2025/11/25/2025-11-14-search-api-updates/

TODO: note here about coveralls and how to invoke manually
"""

import pooch

from time import sleep
from kikuchipy.data._data marshall

# Pre-cache files used in unit tests.
data = kp.data.si_ebsd_moving_screen(0, allow_download=True),
data = kp.data.si_ebsd_moving_screen(5, allow_download=True),
s = kp.data.nickel_ebsd_large(lazy=True, allow_download=True)


def _precache_zenodo():
    """
    Download all datasets hosted on zenodo and handled in kikuchipy via
    pooch. Includeds retry loops to better handle API limitations.
    """

    def retry_and_sleep(url, known_hash, retries=3, sleep_time=30):
        for attempt in range(retries):
            try:
                return pooch.retrieve(
                    url=url,
                    known_hash=known_hash,
                    # large chunk size to reduce requests to Zenodo
                    downloader=pooch.HTTPDownloader(chunk_size=30000),
                    progressbar=False,
                )
            except Exception as e:
                if attempt < retries - 1:
                    print(
                        f"Download failed (attempt {attempt + 1}/{retries}). "
                        f"Retrying in {sleep_time} seconds..."
                    )
                    sleep(sleep_time)
                else:
                    print("All download attempts failed.")
                    raise e
            


    def test_dataset_availability(self):
        """Ping registry URLs of remote repositories (GitHub and Zenodo)
        to check dataset availability.
        """
        datasets = [
            "nickel_ebsd_large/patterns.h5",
            "silicon_ebsd_moving_screen/si_in.h5",
            "silicon_ebsd_moving_screen/si_out5mm.h5",
            "silicon_ebsd_moving_screen/si_out10mm.h5",
            "ebsd_si_wafer.zip",
            "scan1_gain0db.zip",
            "scan2_gain3db.zip",
            "scan3_gain6db.zip",
            "scan4_gain9db.zip",
            "scan5_gain12db.zip",
            "scan6_gain15db.zip",
            "scan7_gain17db.zip",
            "scan8_gain20db.zip",
            "scan9_gain22db.zip",
            "scan10_gain24db.zip",
            "ebsd_master_pattern/al_mc_mp_20kv.h5",
            "ebsd_master_pattern/ni_mc_mp_20kv.h5",
            "ebsd_master_pattern/si_mc_mp_20kv.h5",
            "ebsd_master_pattern/austenite_mc_mp_20kv.h5",
            "ebsd_master_pattern/ferrite_mc_mp_20kv.h5",
            "ebsd_master_pattern/steel_chi_mc_mp_20kv.h5",
            "ebsd_master_pattern/steel_sigma_mc_mp_20kv.h5",
        ]
        for dset in datasets:
            assert marshall.is_available(f"data/{dset}")

def _download_GOS_files(download_all=True):
    """
    Download GOS files for testing purposes and building documentation.

    Parameters
    ----------
    download_all : bool, optional
        If True, download all GOS files. If False, download only recent GOS files.
        Default is True.
    """

    def retry_and_sleep(url, known_hash, retries=3, sleep_time=30):
        for attempt in range(retries):
            try:
                return pooch.retrieve(
                    url=url,
                    known_hash=known_hash,
                    # use large chunk size to reduce number of requests to Zenodo
                    downloader=pooch.HTTPDownloader(chunk_size=30000),
                    progressbar=False,
                )
            except Exception as e:
                if attempt < retries - 1:
                    print(
                        f"Download failed (attempt {attempt + 1}/{retries}). "
                        f"Retrying in {sleep_time} seconds..."
                    )
                    sleep(sleep_time)
                else:
                    print("All download attempts failed.")
                    raise e

    print("Checking if GOS files need downloading...")
    retry_and_sleep(
        url="https://zenodo.org/records/7645765/files/Segger_Guzzinati_Kohl_1.5.0.gosh",
        known_hash="md5:7fee8891c147a4f769668403b54c529b",
    )
    if download_all:
        retry_and_sleep(
            url="https://zenodo.org/records/12800856/files/Dirac_GOS_compact.gosh",
            known_hash="md5:01a855d3750d2c063955248358dbee8d",
        )
        retry_and_sleep(
            url="https://zenodo.org/records/6599071/files/Segger_Guzzinati_Kohl_1.0.0.gos",
            known_hash="md5:d65d5c23142532fde0a80e160ab51574",
        )
    print("GOS files available.")


__all__ = [
    "_download_GOS_files",
]


def __dir__():
    return sorted(__all__)
