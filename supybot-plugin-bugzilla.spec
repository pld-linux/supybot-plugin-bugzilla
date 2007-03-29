Summary:	Bugzilla plugin for Supybot
Name:		Supybot-plugin-Bugzilla
Version:	3.0.0.1
Release:	1
License:	BSD
Group:		Applications/Communications
Source0:	http://supybot.com/Members/mkanat/Bugzilla/3.0.0.1/download/at_download
# Source0-md5:	917a62ea625d56a2bdaec39a120852b2
URL:		http://supybot.com/Members/mkanat/Bugzilla/
BuildRequires:	python >= 1:2.5
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq  python
Requires:	Supybot
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Interacts with multiple Bugzilla installations, including reporting changes
to your Bugzilla by parsing inbound emails. Highly configurable.

This plugin can:
- Fetch details of bugs and attachments and report them to your channel.
- Query your Bugzilla using the QuickSearch syntax and return a limited
  number of results. (Bugzilla 2.22+ only)
- Report changes to your channel by receiving emails from multiple Bugzillas.
- Parse gdb stack traces in newly-filed bugs and report the details
  of the stack trace to the channel.

It supports Bugzilla 2.18 and above (except for the query command, as noted above),
can interface with multiple Bugzillas, and works on multiple networks.

It has lots and lots of configuration options, and all the configuration options
have help, so feel free to read up after loading the plugin itself.

%prep
%setup -q -n Bugzilla

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}/supybot/plugins/Bugzilla

install *.py $RPM_BUILD_ROOT%{py_sitescriptdir}/supybot/plugins/Bugzilla

%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%{py_sitescriptdir}/supybot/plugins/Bugzilla
