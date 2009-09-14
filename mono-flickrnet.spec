Name:           mono-flickrnet
BuildRequires:  mono-devel unzip
Version:        2.1.5
Release:        %mkrel 2
License:        LGPLv2+
URL:		http://www.codeplex.com/FlickrNet
Source:         FlickrNet-25207.zip
Patch0:         assemblyinfo.patch
Group:          Development/Other
Summary:        Flickr.Net API Library
BuildRequires:	mono-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The Flickr.Net API is a .Net Library for accessing the Flickr API. Written entirely in C# it can be accessed from with any .Net language.

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
%__mkdir -p %{buildroot}%{_datadir}/pkgconfig
%__cp flickrnet.pc %{buildroot}%{_datadir}/pkgconfig/

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{_prefix}/lib/mono/flickrnet
%{_prefix}/lib/mono/gac/FlickrNet
%{_datadir}/pkgconfig/flickrnet.pc
