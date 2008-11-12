# Copyright (c) 2008 Simplistix Ltd
#
# This Software is released under the MIT License:
# http://www.opensource.org/licenses/mit-license.html
# See license.txt for more details.

class CellStyle:

    def __init__(self,name,xf):
        self.name = name
        self.xf = xf
        
class Styles:

    def __init__(self,book):
        xfi_to_name = {}
        for name, info in book.style_name_map.items():
            built_in, xfi = info
            assert xfi not in xfi_to_name # should be one-to-one mapping
            xfi_to_name[xfi] = name
        self.cell_styles = {}
        for xfi in xrange(len(book.xf_list)):
            xf = book.xf_list[xfi]
            if xf.is_style:
                continue
            stylexfi = xf.parent_style_index
            assert stylexfi != 4095 # i.e. 0xFFF
            self.cell_styles[xfi] = CellStyle(
                xfi_to_name[stylexfi],
                book.xf_list[stylexfi]
                )
        
    def __getitem__(self,cell):
        return self.cell_styles[cell.xf_index]