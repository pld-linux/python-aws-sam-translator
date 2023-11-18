#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	AWS SAM Translator - library to transform SAM templates into AWS CloudFormation templates
Summary(pl.UTF-8):	AWS SAM Translator - biblioteka do tłumaczenia szablonów SAM do szablonów AWS CloudFormation
Name:		python-aws-sam-translator
# keep 1.42.x here for python2 support
Version:	1.42.0
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/aws-sam-translator/
Source0:	https://files.pythonhosted.org/packages/source/a/aws-sam-translator/aws-sam-translator-%{version}.tar.gz
# Source0-md5:	18b542bd74314014ac71542b77a9ed87
URL:		https://pypi.org/project/aws-sam-translator/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-boto3 >= 1.5
BuildRequires:	python-enum34 >= 1.1
BuildRequires:	python-jsonschema >= 3.2
BuildRequires:	python-mock
BuildRequires:	python-parameterized >= 0.7.4
BuildRequires:	python-pyrsistent >= 0.16.0
BuildRequires:	python-pytest >= 4.6.11
BuildRequires:	python-six >= 1.15
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-boto3 >= 1.5
BuildRequires:	python3-jsonschema >= 3.2
BuildRequires:	python3-parameterized >= 0.7.4
BuildRequires:	python3-pytest >= 6.1.1
BuildRequires:	python3-six >= 1.15
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The AWS Serverless Application Model (SAM) is an open-source framework
for building serverless applications. It provides shorthand syntax to
express functions, APIs, databases, and event source mappings. With
just a few lines of configuration, you can define the application you
want and model it.

%description -l pl.UTF-8
AWS Serverless Application Model (SAM) to mający otwarte źródła
szkielet do budowania bezserwerowych aplikacji. Udostępnia skrótową
składnię do wyrażania funkcji, API, baz danych i odwzorowań źródeł
zdarzeń. Przy użyciu tylko kilku linii konfiguracji można zdefiniować
pożądaną aplikację i ją zamodelować.

%package -n python3-aws-sam-translator
Summary:	AWS SAM Translator - library to transform SAM templates into AWS CloudFormation templates
Summary(pl.UTF-8):	AWS SAM Translator - biblioteka do tłumaczenia szablonów SAM do szablonów AWS CloudFormation
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.6

%description -n python3-aws-sam-translator
The AWS Serverless Application Model (SAM) is an open-source framework
for building serverless applications. It provides shorthand syntax to
express functions, APIs, databases, and event source mappings. With
just a few lines of configuration, you can define the application you
want and model it.

%description -n python3-aws-sam-translator -l pl.UTF-8
AWS Serverless Application Model (SAM) to mający otwarte źródła
szkielet do budowania bezserwerowych aplikacji. Udostępnia skrótową
składnię do wyrażania funkcji, API, baz danych i odwzorowań źródeł
zdarzeń. Przy użyciu tylko kilku linii konfiguracji można zdefiniować
pożądaną aplikację i ją zamodelować.

%prep
%setup -q -n aws-sam-translator-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc NOTICE README.md
%{py_sitescriptdir}/samtranslator
%{py_sitescriptdir}/aws_sam_translator-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-aws-sam-translator
%defattr(644,root,root,755)
%doc NOTICE README.md
%{py3_sitescriptdir}/samtranslator
%{py3_sitescriptdir}/aws_sam_translator-%{version}-py*.egg-info
%endif
