#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_appliance_api import SourceApplianceApi

if __name__ == "__main__":
    source = SourceApplianceApi()
    launch(source, sys.argv[1:])
