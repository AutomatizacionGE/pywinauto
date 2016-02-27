# GUI Application automation and testing library
# Copyright (C) 2015 Intel Corporation
# Copyright (C) 2015 airelil
# Copyright (C) 2009 Mark Mc Mahon
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation; either version 2.1
# of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the
#    Free Software Foundation, Inc.,
#    59 Temple Place,
#    Suite 330,
#    Boston, MA 02111-1307 USA

"""Wraps various UIA windows controls
"""
from . import UIAWrapper
from ..UIAElementInfo import _UIA_dll


#====================================================================
class ButtonWrapper(UIAWrapper.UIAWrapper):
    "Wrap a WPF Button control"

    control_types = [
        _UIA_dll.UIA_ButtonControlTypeId,
        _UIA_dll.UIA_CheckBoxControlTypeId,
        _UIA_dll.UIA_RadioButtonControlTypeId
        ]

    #-----------------------------------------------------------
    def __init__(self, hwnd):
        "Initialize the control"
        super(ButtonWrapper, self).__init__(hwnd)

    #-----------------------------------------------------------
    def toggle(self):
        """
        Toggle a state of a check box control.
        Notice, a radio button control isn't supported by UIA.
        https://msdn.microsoft.com/en-us/library/windows/desktop/ee671290(v=vs.85).aspx
        """
        self._elementInfo.toggle()

    #-----------------------------------------------------------
    def get_toggle_state(self):
        """Get a toggle state of a check box control.
        The toggle state is represented by an integer
        0 - unchecked
        1 - checked
        2 - indeterminate

        The following constants are defined in the UIAElementInfo module
        toggle_state_off = 0
        toggle_state_on = 1
        toggle_state_inderteminate = 2
        """
        return self._elementInfo.toggle_state

    #-----------------------------------------------------------
    def is_dialog(self):
        "Buttons are never dialogs so return False"
        return False

    #-----------------------------------------------------------
    def click(self, *args, **kwargs):
        "Click the Button control by using Invoke pattern"
        self._elementInfo.invoke()
