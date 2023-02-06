#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-glfw
Version  : 2.5.6
Release  : 2
URL      : https://files.pythonhosted.org/packages/91/ed/814be1927191ce943cd27c00c66066605fb8af2e535c5f19a66628f68842/glfw-2.5.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/91/ed/814be1927191ce943cd27c00c66066605fb8af2e535c5f19a66628f68842/glfw-2.5.6.tar.gz
Summary  : A ctypes-based wrapper for GLFW3.
Group    : Development/Tools
License  : MIT
Requires: pypi-glfw-license = %{version}-%{release}
Requires: pypi-glfw-python = %{version}-%{release}
Requires: pypi-glfw-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
pyGLFW
======
This module provides Python bindings for `GLFW <http://www.glfw.org/>`__
(on GitHub: `glfw/glfw <http://github.com/glfw/glfw>`__). It is a
``ctypes`` wrapper which keeps very close to the original GLFW API,
except for:

%package license
Summary: license components for the pypi-glfw package.
Group: Default

%description license
license components for the pypi-glfw package.


%package python
Summary: python components for the pypi-glfw package.
Group: Default
Requires: pypi-glfw-python3 = %{version}-%{release}

%description python
python components for the pypi-glfw package.


%package python3
Summary: python3 components for the pypi-glfw package.
Group: Default
Requires: python3-core
Provides: pypi(glfw)

%description python3
python3 components for the pypi-glfw package.


%prep
%setup -q -n glfw-2.5.6
cd %{_builddir}/glfw-2.5.6
pushd ..
cp -a glfw-2.5.6 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1675645532
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-glfw
cp %{_builddir}/glfw-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-glfw/6a5891f9e1db552a60a1d5d96779d4d97eed61d6 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-glfw/6a5891f9e1db552a60a1d5d96779d4d97eed61d6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
