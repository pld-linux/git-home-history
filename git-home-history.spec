Summary:	a tool to track the history and make backups of your home directory
Name:		git-home-history
# AC_INIT(ghh, 0.1)
Version:	0.1
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	https://github.com/jeanfric/git-home-history/archive/master/%{name}-%{version}.tar.gz
# Source0-md5:	3b55c3ceadc45dc5c1bd70b8d1861f2a
URL:		http://heimdalsgata.com/jeanfric/ghh/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
git-home-history is a tool that simplifies keeping track of changes
you make in your home directory. It is based on the excellent Git
toolkit. git-home-history stores changes you make to your files as
time goes by and can thus provides an easy way to go back to earlier
versions and see changes you made. You can also use it to easily
create backup archives that contain the whole history of your home.

%prep
%setup -qc
mv git-home-history-master/* .

%build
./autogen.sh
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

# no -devel package
%{__rm} $RPM_BUILD_ROOT%{_pkgconfigdir}/ghh.pc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/git-home-history
%attr(755,root,root) %{_bindir}/gtk-ghh
%attr(755,root,root) %{_bindir}/gtk-ghh-commit
%attr(755,root,root) %{_bindir}/gtk-ghh-restore
%{_mandir}/man1/git-home-history.1*
%{_datadir}/ghh
%dir %{_libdir}/ghh
%attr(755,root,root) %{_libdir}/ghh/ghh-service
%{py_sitescriptdir}/ghh
