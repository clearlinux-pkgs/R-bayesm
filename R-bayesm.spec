#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-bayesm
Version  : 3.1.4
Release  : 53
URL      : https://cran.r-project.org/src/contrib/bayesm_3.1-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/bayesm_3.1-4.tar.gz
Summary  : Bayesian Inference for Marketing/Micro-Econometrics
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-bayesm-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-RcppArmadillo
BuildRequires : R-Rcpp
BuildRequires : R-RcppArmadillo
BuildRequires : buildreq-R

%description
in marketing and micro-econometrics applications.

%package lib
Summary: lib components for the R-bayesm package.
Group: Libraries

%description lib
lib components for the R-bayesm package.


%prep
%setup -q -c -n bayesm
cd %{_builddir}/bayesm

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640976097

%install
export SOURCE_DATE_EPOCH=1640976097
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bayesm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bayesm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bayesm
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/bayesm/DESCRIPTION
/usr/lib64/R/library/bayesm/INDEX
/usr/lib64/R/library/bayesm/Meta/Rd.rds
/usr/lib64/R/library/bayesm/Meta/data.rds
/usr/lib64/R/library/bayesm/Meta/features.rds
/usr/lib64/R/library/bayesm/Meta/hsearch.rds
/usr/lib64/R/library/bayesm/Meta/links.rds
/usr/lib64/R/library/bayesm/Meta/nsInfo.rds
/usr/lib64/R/library/bayesm/Meta/package.rds
/usr/lib64/R/library/bayesm/Meta/vignette.rds
/usr/lib64/R/library/bayesm/NAMESPACE
/usr/lib64/R/library/bayesm/R/bayesm
/usr/lib64/R/library/bayesm/R/bayesm.rdb
/usr/lib64/R/library/bayesm/R/bayesm.rdx
/usr/lib64/R/library/bayesm/data/Scotch.rda
/usr/lib64/R/library/bayesm/data/bank.rda
/usr/lib64/R/library/bayesm/data/camera.RData
/usr/lib64/R/library/bayesm/data/cheese.rda
/usr/lib64/R/library/bayesm/data/customerSat.rda
/usr/lib64/R/library/bayesm/data/detailing.rda
/usr/lib64/R/library/bayesm/data/margarine.rda
/usr/lib64/R/library/bayesm/data/orangeJuice.rda
/usr/lib64/R/library/bayesm/data/tuna.rda
/usr/lib64/R/library/bayesm/doc/Constrained_MNL_Vignette.R
/usr/lib64/R/library/bayesm/doc/Constrained_MNL_Vignette.Rmd
/usr/lib64/R/library/bayesm/doc/Constrained_MNL_Vignette.html
/usr/lib64/R/library/bayesm/doc/bayesm_Overview_Vignette.R
/usr/lib64/R/library/bayesm/doc/bayesm_Overview_Vignette.Rmd
/usr/lib64/R/library/bayesm/doc/bayesm_Overview_Vignette.html
/usr/lib64/R/library/bayesm/doc/index.html
/usr/lib64/R/library/bayesm/help/AnIndex
/usr/lib64/R/library/bayesm/help/aliases.rds
/usr/lib64/R/library/bayesm/help/bayesm.rdb
/usr/lib64/R/library/bayesm/help/bayesm.rdx
/usr/lib64/R/library/bayesm/help/paths.rds
/usr/lib64/R/library/bayesm/html/00Index.html
/usr/lib64/R/library/bayesm/html/R.css
/usr/lib64/R/library/bayesm/include/bayesm.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/bayesm/libs/bayesm.so
/usr/lib64/R/library/bayesm/libs/bayesm.so.avx2
/usr/lib64/R/library/bayesm/libs/bayesm.so.avx512
