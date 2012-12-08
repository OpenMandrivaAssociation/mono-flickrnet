Summary:	Flickr.Net API Library
Name:		mono-flickrnet
Version:	2.1.5
Release:	5
Group:		Development/Other
License:	LGPLv2+
URL:		http://www.codeplex.com/FlickrNet
Source:		FlickrNet-25207.zip
Patch0:		assemblyinfo.patch
BuildRequires:	mono-devel
BuildRequires:	unzip
BuildArch:	noarch

%description
The Flickr.Net API is a .Net Library for accessing the Flickr API.
Written entirely in C# it can be accessed from with any .Net language.

%prep
%setup -n FlickrNet -q
%patch0 -p1

%build
gmcs -debug -target:library -out:FlickrNet.dll  -r:System.Web.dll -r:System.Drawing.dll *.cs
cat << EOF > flickrnet.pc
prefix=%{_prefix}
assemblies_dir=\${prefix}/lib/mono/flickrnet
Libraries=\${assemblies_dir}/FlickrNet.dll
 
Name: FlickrNet
Description: Flickr.Net API Library
Version: %{version}
Libs: -r:\${assemblies_dir}/FlickrNet.dll
EOF

%install
gacutil -i FlickrNet.dll -package flickrnet -root %{buildroot}%{_prefix}/lib
mkdir -p %{buildroot}%{_datadir}/pkgconfig
cp flickrnet.pc %{buildroot}%{_datadir}/pkgconfig/

%files
%{_prefix}/lib/mono/flickrnet
%{_prefix}/lib/mono/gac/FlickrNet
%{_datadir}/pkgconfig/flickrnet.pc


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.1.5-4mdv2011.0
+ Revision: 666479
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1.5-3mdv2011.0
+ Revision: 609163
- rebuild

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 2.1.5-2mdv2010.0
+ Revision: 440086
- rebuild

* Sun Feb 01 2009 Funda Wang <fwang@mandriva.org> 2.1.5-1mdv2009.1
+ Revision: 336235
- import mono-flickrnet


