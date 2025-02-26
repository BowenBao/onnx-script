# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------

"""Typings for function definitions."""

from __future__ import annotations

from typing import TypeVar, Union

from onnxscript import (
    BFLOAT16,
    BOOL,
    COMPLEX64,
    COMPLEX128,
    DOUBLE,
    FLOAT,
    FLOAT16,
    INT8,
    INT16,
    INT32,
    INT64,
    UINT8,
)

# NOTE: We do not care about unsigned types beyond UINT8 because PyTorch does not us them.

_TensorType = Union[
    BFLOAT16,
    BOOL,
    COMPLEX64,
    COMPLEX128,
    DOUBLE,
    FLOAT,
    FLOAT16,
    INT8,
    INT16,
    INT32,
    INT64,
    UINT8,
]
_FloatType = Union[FLOAT16, FLOAT, DOUBLE]
IntType = Union[INT8, INT16, INT32, INT64]
RealType = Union[
    BFLOAT16,
    FLOAT16,
    FLOAT,
    DOUBLE,
    INT8,
    INT16,
    INT32,
    INT64,
]

TTensor = TypeVar("TTensor", bound=_TensorType)
TFloat = TypeVar("TFloat", bound=_FloatType)
TFloatOrBFloat16 = TypeVar("TFloatOrBFloat16", bound=Union[FLOAT16, FLOAT, DOUBLE, BFLOAT16])
TInt = TypeVar("TInt", bound=IntType)
TReal = TypeVar("TReal", bound=RealType)
TRealUnlessInt16OrInt8 = TypeVar(
    "TRealUnlessInt16OrInt8", bound=Union[FLOAT16, FLOAT, DOUBLE, BFLOAT16, INT32, INT64]
)
TRealUnlessFloat16OrInt8 = TypeVar(
    "TRealUnlessFloat16OrInt8", bound=Union[DOUBLE, FLOAT, INT16, INT32, INT64]
)
