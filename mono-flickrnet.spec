Summary:	Flickr.Net API Library
Name:		mono-flickrnet
Version:	2.1.5
Release:	12
Group:		Development/Other
License:	LGPLv2+
Url:		http://www.codeplex.com/FlickrNet
Source0:	FlickrNet-25207.zip
Patch0:		assemblyinfo.patch
BuildArch:	noarch
BuildRequires:	unzip
BuildRequires:	pkgconfig(mono)

%description
The Flickr.Net API is a .Net Library for accessing the Flickr API.
Written entirely in C# it can be accessed from with any .Net language.

%prep
%setup -n FlickrNet -q
%apply_patches

%build
gmcs -debug -target:library -out:FlickrNet.dll  -r:System.Web.dll -r:System.Drawing.dll *.cs
cat << EOF > flickrnet.pc
prefix=%{_prefix}
assemblies_dir=\${prefix}/lib/mono/flickrnet
Libraries=\${assemblies_dir}/FlickrNet.dll
 
Name:		FlickrNet
Description:	Flickr.Net API Library
Version:	%{version}
Libs:	-r:\${assemblies_dir}/FlickrNet.dll
EOF

%install
gacutil -i FlickrNet.dll -package flickrnet -root %{buildroot}%{_prefix}/lib
mkdir -p %{buildroot}%{_datadir}/pkgconfig
cp flickrnet.pc %{buildroot}%{_datadir}/pkgconfig/

%files
%{_prefix}/lib/mono/flickrnet
%{_prefix}/lib/mono/gac/FlickrNet
%{_datadir}/pkgconfig/flickrnet.pc

