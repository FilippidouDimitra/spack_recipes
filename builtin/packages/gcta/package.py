# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Gcta(Package):

    """GCTA (Genome-wide Complex Trait Analysis) was originally designed to
    estimate the proportion of phenotypic variance explained by all genome-wide
    SNPs for complex traits (the GREML method), and has subsequently extended
    for many other analyses to better understand the genetic architecture of
    complex traits. GCTA currently supports the following analyses."""

    url      = "https://github.com/jianyangqt/gcta/releases/download/v1.94.0beta/gcta_v1.94.0Beta_linux_kernel_4_x86_64_static"

    version('1.94.0beta','bc64255da3dd740a6017b93d140a75ff207fc74ce16ac8507f2ca9ee359b48d8', preferred=True, expand=False)
    version('1.91.2beta_mac', 'ce0882ad35dd9474ffe40911da369274700af1ecb9916c0a355b7bad14850234')
    version('1.91.2beta', '192efb767be1c7ca9c2dac5d2c2317a97c7a9db1f801168d19ad2a51b98d9b10')

    conflicts('@1.91.2beta', when='platform=darwin')
    conflicts('@1.91.2beta_mac', when='platform=linux')

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install('gcta_v1.94.0Beta_linux_kernel_4_x86_64_static', join_path(prefix.bin, 'gcta64'))
        set_executable(join_path(prefix.bin, 'gcta64'))
