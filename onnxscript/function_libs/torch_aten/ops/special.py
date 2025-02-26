# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------
# mypy: disable-error-code="misc,arg-type,type-arg,valid-type,assignment,return-value"
"""torch.ops.aten operators under the `special` module.

- No inplace operators.
- All functions should not have the script() decorator. This is because
    we want to delay the compilation of the function.
"""
from __future__ import annotations

from typing import Optional, Sequence

from onnxscript.onnx_types import TensorType


def aten_special_airy_ai(x: TensorType) -> TensorType:
    # special_airy_ai(Tensor x) -> Tensor

    raise NotImplementedError()


def aten_special_bessel_j0(self: TensorType) -> TensorType:
    # special_bessel_j0(Tensor self) -> Tensor

    raise NotImplementedError()


def aten_special_bessel_j1(self: TensorType) -> TensorType:
    # special_bessel_j1(Tensor self) -> Tensor

    raise NotImplementedError()


def aten_special_bessel_y0(self: TensorType) -> TensorType:
    # special_bessel_y0(Tensor self) -> Tensor

    raise NotImplementedError()


def aten_special_bessel_y1(self: TensorType) -> TensorType:
    # special_bessel_y1(Tensor self) -> Tensor

    raise NotImplementedError()


def aten_special_chebyshev_polynomial_t(x: TensorType, n: TensorType) -> TensorType:
    # special_chebyshev_polynomial_t(Tensor x, Tensor n) -> Tensor

    raise NotImplementedError()


def aten_special_chebyshev_polynomial_u(x: TensorType, n: TensorType) -> TensorType:
    # special_chebyshev_polynomial_u(Tensor x, Tensor n) -> Tensor

    raise NotImplementedError()


def aten_special_chebyshev_polynomial_v(x: TensorType, n: TensorType) -> TensorType:
    # special_chebyshev_polynomial_v(Tensor x, Tensor n) -> Tensor

    raise NotImplementedError()


def aten_special_chebyshev_polynomial_w(x: TensorType, n: TensorType) -> TensorType:
    # special_chebyshev_polynomial_w(Tensor x, Tensor n) -> Tensor

    raise NotImplementedError()


def aten_special_digamma(self: TensorType) -> TensorType:
    # special_digamma(Tensor self) -> Tensor

    raise NotImplementedError()


def aten_special_entr(self: TensorType) -> TensorType:
    # special_entr(Tensor self) -> Tensor

    raise NotImplementedError()


def aten_special_erf(self: TensorType) -> TensorType:
    # special_erf(Tensor self) -> Tensor

    raise NotImplementedError()


def aten_special_erfc(self: TensorType) -> TensorType:
    # special_erfc(Tensor self) -> Tensor

    raise NotImplementedError()


def aten_special_erfcx(self: TensorType) -> TensorType:
    # special_erfcx(Tensor self) -> Tensor

    raise NotImplementedError()


def aten_special_erfinv(self: TensorType) -> TensorType:
    # special_erfinv(Tensor self) -> Tensor

    raise NotImplementedError()


def aten_special_exp2(self: TensorType) -> TensorType:
    # special_exp2(Tensor self) -> Tensor

    raise NotImplementedError()


def aten_special_expit(self: TensorType) -> TensorType:
    # special_expit(Tensor self) -> Tensor

    raise NotImplementedError()


def aten_special_expm1(self: TensorType) -> TensorType:
    # special_expm1(Tensor self) -> Tensor

    raise NotImplementedError()


def aten_special_gammainc(self: TensorType, other: TensorType) -> TensorType:
    # special_gammainc(Tensor self, Tensor other) -> Tensor

    raise NotImplementedError()


def aten_special_gammaincc(self: TensorType, other: TensorType) -> TensorType:
    # special_gammaincc(Tensor self, Tensor other) -> Tensor

    raise NotImplementedError()


def aten_special_gammaln(self: TensorType) -> TensorType:
    # special_gammaln(Tensor self) -> Tensor

    raise NotImplementedError()


def aten_special_hermite_polynomial_h(x: TensorType, n: TensorType) -> TensorType:
    # special_hermite_polynomial_h(Tensor x, Tensor n) -> Tensor

    raise NotImplementedError()


def aten_special_hermite_polynomial_he(x: TensorType, n: TensorType) -> TensorType:
    # special_hermite_polynomial_he(Tensor x, Tensor n) -> Tensor

    raise NotImplementedError()


def aten_special_i0(self: TensorType) -> TensorType:
    # special_i0(Tensor self) -> Tensor

    raise NotImplementedError()


def aten_special_i0e(self: TensorType) -> TensorType:
    # special_i0e(Tensor self) -> Tensor

    raise NotImplementedError()


def aten_special_i1(self: TensorType) -> TensorType:
    # special_i1(Tensor self) -> Tensor

    raise NotImplementedError()


def aten_special_i1e(self: TensorType) -> TensorType:
    # special_i1e(Tensor self) -> Tensor

    raise NotImplementedError()


def aten_special_laguerre_polynomial_l(x: TensorType, n: TensorType) -> TensorType:
    # special_laguerre_polynomial_l(Tensor x, Tensor n) -> Tensor

    raise NotImplementedError()


def aten_special_legendre_polynomial_p(x: TensorType, n: TensorType) -> TensorType:
    # special_legendre_polynomial_p(Tensor x, Tensor n) -> Tensor

    raise NotImplementedError()


def aten_special_log1p(self: TensorType) -> TensorType:
    # special_log1p(Tensor self) -> Tensor

    raise NotImplementedError()


def aten_special_log_ndtr(self: TensorType) -> TensorType:
    # special_log_ndtr(Tensor self) -> Tensor

    raise NotImplementedError()


def aten_special_log_softmax(self: TensorType, dim: int, dtype: int = -1) -> TensorType:
    # special_log_softmax(Tensor self, int dim, *, ScalarType? dtype=None) -> Tensor

    raise NotImplementedError()


def aten_special_logit(self: TensorType, eps: Optional[float] = None) -> TensorType:
    # special_logit(Tensor self, float? eps=None) -> Tensor

    raise NotImplementedError()


def aten_special_logsumexp(
    self: TensorType, dim: Sequence[int], keepdim: bool = False
) -> TensorType:
    # special_logsumexp(Tensor self, int[1] dim, bool keepdim=False) -> Tensor

    raise NotImplementedError()


def aten_special_modified_bessel_i0(self: TensorType) -> TensorType:
    # special_modified_bessel_i0(Tensor self) -> Tensor

    raise NotImplementedError()


def aten_special_modified_bessel_i1(self: TensorType) -> TensorType:
    # special_modified_bessel_i1(Tensor self) -> Tensor

    raise NotImplementedError()


def aten_special_modified_bessel_k0(self: TensorType) -> TensorType:
    # special_modified_bessel_k0(Tensor self) -> Tensor

    raise NotImplementedError()


def aten_special_modified_bessel_k1(self: TensorType) -> TensorType:
    # special_modified_bessel_k1(Tensor self) -> Tensor

    raise NotImplementedError()


def aten_special_multigammaln(self: TensorType, p: int) -> TensorType:
    # special_multigammaln(Tensor self, int p) -> Tensor

    raise NotImplementedError()


def aten_special_ndtr(self: TensorType) -> TensorType:
    # special_ndtr(Tensor self) -> Tensor

    raise NotImplementedError()


def aten_special_ndtri(self: TensorType) -> TensorType:
    # special_ndtri(Tensor self) -> Tensor

    raise NotImplementedError()


def aten_special_polygamma(n: int, self: TensorType) -> TensorType:
    # special_polygamma(int n, Tensor self) -> Tensor

    raise NotImplementedError()


def aten_special_psi(self: TensorType) -> TensorType:
    # special_psi(Tensor self) -> Tensor

    raise NotImplementedError()


def aten_special_round(self: TensorType, decimals: int = 0) -> TensorType:
    # special_round(Tensor self, *, int decimals=0) -> Tensor

    raise NotImplementedError()


def aten_special_scaled_modified_bessel_k0(x: TensorType) -> TensorType:
    # special_scaled_modified_bessel_k0(Tensor x) -> Tensor

    raise NotImplementedError()


def aten_special_scaled_modified_bessel_k1(x: TensorType) -> TensorType:
    # special_scaled_modified_bessel_k1(Tensor x) -> Tensor

    raise NotImplementedError()


def aten_special_shifted_chebyshev_polynomial_t(x: TensorType, n: TensorType) -> TensorType:
    # special_shifted_chebyshev_polynomial_t(Tensor x, Tensor n) -> Tensor

    raise NotImplementedError()


def aten_special_shifted_chebyshev_polynomial_u(x: TensorType, n: TensorType) -> TensorType:
    # special_shifted_chebyshev_polynomial_u(Tensor x, Tensor n) -> Tensor

    raise NotImplementedError()


def aten_special_shifted_chebyshev_polynomial_v(x: TensorType, n: TensorType) -> TensorType:
    # special_shifted_chebyshev_polynomial_v(Tensor x, Tensor n) -> Tensor

    raise NotImplementedError()


def aten_special_shifted_chebyshev_polynomial_w(x: TensorType, n: TensorType) -> TensorType:
    # special_shifted_chebyshev_polynomial_w(Tensor x, Tensor n) -> Tensor

    raise NotImplementedError()


def aten_special_sinc(self: TensorType) -> TensorType:
    # special_sinc(Tensor self) -> Tensor

    raise NotImplementedError()


def aten_special_softmax(
    self: TensorType, dim: int, dtype: Optional[int] = None
) -> TensorType:
    # special_softmax(Tensor self, int dim, ScalarType? dtype=None) -> Tensor

    raise NotImplementedError()


def aten_special_spherical_bessel_j0(x: TensorType) -> TensorType:
    # special_spherical_bessel_j0(Tensor x) -> Tensor

    raise NotImplementedError()


def aten_special_xlog1py(self: TensorType, other: TensorType) -> TensorType:
    # special_xlog1py(Tensor self, Tensor other) -> Tensor

    raise NotImplementedError()


def aten_special_xlogy(self: TensorType, other: TensorType) -> TensorType:
    # special_xlogy(Tensor self, Tensor other) -> Tensor

    raise NotImplementedError()


def aten_special_zeta(self: TensorType, other: TensorType) -> TensorType:
    # special_zeta(Tensor self, Tensor other) -> Tensor

    raise NotImplementedError()
