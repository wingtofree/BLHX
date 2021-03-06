#pragma once

#include <boost/python.hpp>
#include <boost/python/numpy.hpp>

#include "GraphCap/Image.h"

namespace pygc
{
	namespace py = boost::python;
	namespace np = boost::python::numpy;

	enum ByteOrder
	{
		BO_UNKNOWN,
		BO_BGR,		// B在低位，R在高位，OpenCV默认格式
		BO_RGB,		// R在低位，B在高位
		BO_MAXCOUNT
	};

	class pyImage :
		public Image
	{
	public:
		pyImage();

		virtual void convertFromD3D11Texture2D(CComPtr<ID3D11DeviceContext> deviceContext,
			CComPtr<ID3D11Texture2D> texture2D) override;

		np::ndarray toNdarray();

	private:
		int_t m_width;
		int_t m_height;
		int_t m_bpp;
		py::tuple m_shape;
		np::dtype m_dtype;
		np::ndarray m_ndarray;
	};
}
