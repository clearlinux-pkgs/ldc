#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ldc
Version  : 1.17.0
Release  : 17
URL      : https://github.com/ldc-developers/ldc/releases/download/v1.17.0/ldc-1.17.0-src.tar.gz
Source0  : https://github.com/ldc-developers/ldc/releases/download/v1.17.0/ldc-1.17.0-src.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause BSL-1.0
Requires: ldc-bin = %{version}-%{release}
Requires: ldc-data = %{version}-%{release}
Requires: ldc-lib = %{version}-%{release}
Requires: ldc-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : ldc
BuildRequires : ldc-dev
BuildRequires : libffi-dev
BuildRequires : llvm
BuildRequires : llvm-dev
BuildRequires : llvm-extras
BuildRequires : llvm-staticdev
BuildRequires : ncurses-dev
BuildRequires : pkg-config
BuildRequires : strace
Patch1: 0001-Fixups-for-packaging-and-stateless-config.patch
Patch2: 0002-Don-t-force-the-use-of-gold-linker.patch
Patch3: 0003-Add-support-for-LLVM-9.0.0.patch

%description
This is a standalone (DMD-style) binary package for LDC, the LLVM-based D
compiler.

%package bin
Summary: bin components for the ldc package.
Group: Binaries
Requires: ldc-data = %{version}-%{release}
Requires: ldc-license = %{version}-%{release}

%description bin
bin components for the ldc package.


%package data
Summary: data components for the ldc package.
Group: Data

%description data
data components for the ldc package.


%package dev
Summary: dev components for the ldc package.
Group: Development
Requires: ldc-lib = %{version}-%{release}
Requires: ldc-bin = %{version}-%{release}
Requires: ldc-data = %{version}-%{release}
Provides: ldc-devel = %{version}-%{release}
Requires: ldc = %{version}-%{release}

%description dev
dev components for the ldc package.


%package lib
Summary: lib components for the ldc package.
Group: Libraries
Requires: ldc-data = %{version}-%{release}
Requires: ldc-license = %{version}-%{release}

%description lib
lib components for the ldc package.


%package license
Summary: license components for the ldc package.
Group: Default

%description license
license components for the ldc package.


%prep
%setup -q -n ldc-1.17.0-src
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
## build_prepend content
export CFLAGS="$CFLAGS -fPIC "
export LDFLAGS="$LDFLAGS -fPIC "
export CXXFLAGS="$CXXFLAGS -fPIC"
export LD=/usr/bin/ld
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570163293
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CC=clang
export CXX=clang++
export LD=ld.gold
export CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error -Wl,-z,max-page-size=0x1000 -march=westmere -mtune=haswell"
export CXXFLAGS=$CFLAGS
unset LDFLAGS
unset LDFLAGS
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake .. -DLDC_ENABLE_PLUGINS=ON \
-DLDC_WITH_LLD=OFF \
-DBUILD_SHARED_LIBS:BOOL=ON \
-DLDC_DYNAMIC_COMPILE=OFF \
-DSYSCONF_INSTALL_DIR=/usr/share/defaults/etc
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1570163293
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ldc
cp LICENSE %{buildroot}/usr/share/package-licenses/ldc/LICENSE
cp runtime/druntime/LICENSE.txt %{buildroot}/usr/share/package-licenses/ldc/runtime_druntime_LICENSE.txt
cp runtime/phobos/LICENSE_1_0.txt %{buildroot}/usr/share/package-licenses/ldc/runtime_phobos_LICENSE_1_0.txt
pushd clr-build
%make_install
popd
## install_append content
mkdir -p %{buildroot}/usr/share/bash-completion/completions
mv %{buildroot}/usr/share/defaults/etc/bash_completion.d/ldc2 %{buildroot}/usr/share/bash-completion/completions/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ldc-build-runtime
/usr/bin/ldc-prune-cache
/usr/bin/ldc2
/usr/bin/ldmd2

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/ldc2
/usr/share/defaults/etc/ldc2.conf

%files dev
%defattr(-,root,root,-)
/usr/include/d/core/atomic.d
/usr/include/d/core/attribute.d
/usr/include/d/core/bitop.d
/usr/include/d/core/checkedint.d
/usr/include/d/core/cpuid.d
/usr/include/d/core/demangle.d
/usr/include/d/core/exception.d
/usr/include/d/core/gc/config.d
/usr/include/d/core/gc/gcinterface.d
/usr/include/d/core/gc/registry.d
/usr/include/d/core/internal/abort.d
/usr/include/d/core/internal/arrayop.d
/usr/include/d/core/internal/convert.d
/usr/include/d/core/internal/dassert.d
/usr/include/d/core/internal/hash.d
/usr/include/d/core/internal/lifetime.d
/usr/include/d/core/internal/parseoptions.d
/usr/include/d/core/internal/spinlock.d
/usr/include/d/core/internal/string.d
/usr/include/d/core/internal/traits.d
/usr/include/d/core/internal/utf.d
/usr/include/d/core/lifetime.d
/usr/include/d/core/math.d
/usr/include/d/core/memory.d
/usr/include/d/core/runtime.d
/usr/include/d/core/simd.d
/usr/include/d/core/stdc/assert_.d
/usr/include/d/core/stdc/complex.d
/usr/include/d/core/stdc/config.d
/usr/include/d/core/stdc/ctype.d
/usr/include/d/core/stdc/errno.d
/usr/include/d/core/stdc/fenv.d
/usr/include/d/core/stdc/float_.d
/usr/include/d/core/stdc/inttypes.d
/usr/include/d/core/stdc/limits.d
/usr/include/d/core/stdc/locale.d
/usr/include/d/core/stdc/math.d
/usr/include/d/core/stdc/signal.d
/usr/include/d/core/stdc/stdarg.d
/usr/include/d/core/stdc/stddef.d
/usr/include/d/core/stdc/stdint.d
/usr/include/d/core/stdc/stdio.d
/usr/include/d/core/stdc/stdlib.d
/usr/include/d/core/stdc/string.d
/usr/include/d/core/stdc/tgmath.d
/usr/include/d/core/stdc/time.d
/usr/include/d/core/stdc/wchar_.d
/usr/include/d/core/stdc/wctype.d
/usr/include/d/core/stdcpp/allocator.d
/usr/include/d/core/stdcpp/array.d
/usr/include/d/core/stdcpp/exception.d
/usr/include/d/core/stdcpp/new_.d
/usr/include/d/core/stdcpp/string_view.d
/usr/include/d/core/stdcpp/type_traits.d
/usr/include/d/core/stdcpp/typeinfo.d
/usr/include/d/core/stdcpp/xutility.d
/usr/include/d/core/sync/barrier.d
/usr/include/d/core/sync/condition.d
/usr/include/d/core/sync/config.d
/usr/include/d/core/sync/event.d
/usr/include/d/core/sync/exception.d
/usr/include/d/core/sync/mutex.d
/usr/include/d/core/sync/rwmutex.d
/usr/include/d/core/sync/semaphore.d
/usr/include/d/core/sys/bionic/fcntl.d
/usr/include/d/core/sys/bionic/string.d
/usr/include/d/core/sys/bionic/unistd.d
/usr/include/d/core/sys/darwin/crt_externs.d
/usr/include/d/core/sys/darwin/dlfcn.d
/usr/include/d/core/sys/darwin/execinfo.d
/usr/include/d/core/sys/darwin/mach/dyld.d
/usr/include/d/core/sys/darwin/mach/getsect.d
/usr/include/d/core/sys/darwin/mach/kern_return.d
/usr/include/d/core/sys/darwin/mach/loader.d
/usr/include/d/core/sys/darwin/mach/port.d
/usr/include/d/core/sys/darwin/mach/semaphore.d
/usr/include/d/core/sys/darwin/mach/thread_act.d
/usr/include/d/core/sys/darwin/netinet/in_.d
/usr/include/d/core/sys/darwin/pthread.d
/usr/include/d/core/sys/darwin/string.d
/usr/include/d/core/sys/darwin/sys/cdefs.d
/usr/include/d/core/sys/darwin/sys/event.d
/usr/include/d/core/sys/darwin/sys/mman.d
/usr/include/d/core/sys/dragonflybsd/dlfcn.d
/usr/include/d/core/sys/dragonflybsd/execinfo.d
/usr/include/d/core/sys/dragonflybsd/netinet/in_.d
/usr/include/d/core/sys/dragonflybsd/pthread_np.d
/usr/include/d/core/sys/dragonflybsd/string.d
/usr/include/d/core/sys/dragonflybsd/sys/_bitset.d
/usr/include/d/core/sys/dragonflybsd/sys/_cpuset.d
/usr/include/d/core/sys/dragonflybsd/sys/cdefs.d
/usr/include/d/core/sys/dragonflybsd/sys/elf.d
/usr/include/d/core/sys/dragonflybsd/sys/elf32.d
/usr/include/d/core/sys/dragonflybsd/sys/elf64.d
/usr/include/d/core/sys/dragonflybsd/sys/elf_common.d
/usr/include/d/core/sys/dragonflybsd/sys/event.d
/usr/include/d/core/sys/dragonflybsd/sys/link_elf.d
/usr/include/d/core/sys/dragonflybsd/sys/mman.d
/usr/include/d/core/sys/dragonflybsd/time.d
/usr/include/d/core/sys/freebsd/dlfcn.d
/usr/include/d/core/sys/freebsd/execinfo.d
/usr/include/d/core/sys/freebsd/netinet/in_.d
/usr/include/d/core/sys/freebsd/pthread_np.d
/usr/include/d/core/sys/freebsd/string.d
/usr/include/d/core/sys/freebsd/sys/_bitset.d
/usr/include/d/core/sys/freebsd/sys/_cpuset.d
/usr/include/d/core/sys/freebsd/sys/cdefs.d
/usr/include/d/core/sys/freebsd/sys/elf.d
/usr/include/d/core/sys/freebsd/sys/elf32.d
/usr/include/d/core/sys/freebsd/sys/elf64.d
/usr/include/d/core/sys/freebsd/sys/elf_common.d
/usr/include/d/core/sys/freebsd/sys/event.d
/usr/include/d/core/sys/freebsd/sys/link_elf.d
/usr/include/d/core/sys/freebsd/sys/mman.d
/usr/include/d/core/sys/freebsd/sys/mount.d
/usr/include/d/core/sys/freebsd/time.d
/usr/include/d/core/sys/freebsd/unistd.d
/usr/include/d/core/sys/linux/config.d
/usr/include/d/core/sys/linux/dlfcn.d
/usr/include/d/core/sys/linux/elf.d
/usr/include/d/core/sys/linux/epoll.d
/usr/include/d/core/sys/linux/errno.d
/usr/include/d/core/sys/linux/execinfo.d
/usr/include/d/core/sys/linux/fcntl.d
/usr/include/d/core/sys/linux/ifaddrs.d
/usr/include/d/core/sys/linux/link.d
/usr/include/d/core/sys/linux/netinet/in_.d
/usr/include/d/core/sys/linux/netinet/tcp.d
/usr/include/d/core/sys/linux/sched.d
/usr/include/d/core/sys/linux/stdio.d
/usr/include/d/core/sys/linux/string.d
/usr/include/d/core/sys/linux/sys/auxv.d
/usr/include/d/core/sys/linux/sys/eventfd.d
/usr/include/d/core/sys/linux/sys/file.d
/usr/include/d/core/sys/linux/sys/inotify.d
/usr/include/d/core/sys/linux/sys/mman.d
/usr/include/d/core/sys/linux/sys/netinet/tcp.d
/usr/include/d/core/sys/linux/sys/prctl.d
/usr/include/d/core/sys/linux/sys/signalfd.d
/usr/include/d/core/sys/linux/sys/socket.d
/usr/include/d/core/sys/linux/sys/sysinfo.d
/usr/include/d/core/sys/linux/sys/time.d
/usr/include/d/core/sys/linux/sys/xattr.d
/usr/include/d/core/sys/linux/termios.d
/usr/include/d/core/sys/linux/time.d
/usr/include/d/core/sys/linux/timerfd.d
/usr/include/d/core/sys/linux/tipc.d
/usr/include/d/core/sys/linux/unistd.d
/usr/include/d/core/sys/netbsd/dlfcn.d
/usr/include/d/core/sys/netbsd/execinfo.d
/usr/include/d/core/sys/netbsd/string.d
/usr/include/d/core/sys/netbsd/sys/elf.d
/usr/include/d/core/sys/netbsd/sys/elf32.d
/usr/include/d/core/sys/netbsd/sys/elf64.d
/usr/include/d/core/sys/netbsd/sys/elf_common.d
/usr/include/d/core/sys/netbsd/sys/event.d
/usr/include/d/core/sys/netbsd/sys/featuretest.d
/usr/include/d/core/sys/netbsd/sys/link_elf.d
/usr/include/d/core/sys/netbsd/sys/mman.d
/usr/include/d/core/sys/netbsd/time.d
/usr/include/d/core/sys/openbsd/dlfcn.d
/usr/include/d/core/sys/openbsd/string.d
/usr/include/d/core/sys/openbsd/sys/cdefs.d
/usr/include/d/core/sys/openbsd/sys/elf.d
/usr/include/d/core/sys/openbsd/sys/elf32.d
/usr/include/d/core/sys/openbsd/sys/elf64.d
/usr/include/d/core/sys/openbsd/sys/elf_common.d
/usr/include/d/core/sys/openbsd/sys/link_elf.d
/usr/include/d/core/sys/openbsd/sys/mman.d
/usr/include/d/core/sys/openbsd/time.d
/usr/include/d/core/sys/posix/aio.d
/usr/include/d/core/sys/posix/arpa/inet.d
/usr/include/d/core/sys/posix/config.d
/usr/include/d/core/sys/posix/dirent.d
/usr/include/d/core/sys/posix/dlfcn.d
/usr/include/d/core/sys/posix/fcntl.d
/usr/include/d/core/sys/posix/grp.d
/usr/include/d/core/sys/posix/iconv.d
/usr/include/d/core/sys/posix/inttypes.d
/usr/include/d/core/sys/posix/libgen.d
/usr/include/d/core/sys/posix/mqueue.d
/usr/include/d/core/sys/posix/net/if_.d
/usr/include/d/core/sys/posix/netdb.d
/usr/include/d/core/sys/posix/netinet/in_.d
/usr/include/d/core/sys/posix/netinet/tcp.d
/usr/include/d/core/sys/posix/poll.d
/usr/include/d/core/sys/posix/pthread.d
/usr/include/d/core/sys/posix/pwd.d
/usr/include/d/core/sys/posix/sched.d
/usr/include/d/core/sys/posix/semaphore.d
/usr/include/d/core/sys/posix/setjmp.d
/usr/include/d/core/sys/posix/signal.d
/usr/include/d/core/sys/posix/spawn.d
/usr/include/d/core/sys/posix/stdio.d
/usr/include/d/core/sys/posix/stdlib.d
/usr/include/d/core/sys/posix/sys/filio.d
/usr/include/d/core/sys/posix/sys/ioccom.d
/usr/include/d/core/sys/posix/sys/ioctl.d
/usr/include/d/core/sys/posix/sys/ipc.d
/usr/include/d/core/sys/posix/sys/mman.d
/usr/include/d/core/sys/posix/sys/msg.d
/usr/include/d/core/sys/posix/sys/resource.d
/usr/include/d/core/sys/posix/sys/select.d
/usr/include/d/core/sys/posix/sys/shm.d
/usr/include/d/core/sys/posix/sys/socket.d
/usr/include/d/core/sys/posix/sys/stat.d
/usr/include/d/core/sys/posix/sys/statvfs.d
/usr/include/d/core/sys/posix/sys/time.d
/usr/include/d/core/sys/posix/sys/ttycom.d
/usr/include/d/core/sys/posix/sys/types.d
/usr/include/d/core/sys/posix/sys/uio.d
/usr/include/d/core/sys/posix/sys/un.d
/usr/include/d/core/sys/posix/sys/utsname.d
/usr/include/d/core/sys/posix/sys/wait.d
/usr/include/d/core/sys/posix/syslog.d
/usr/include/d/core/sys/posix/termios.d
/usr/include/d/core/sys/posix/time.d
/usr/include/d/core/sys/posix/ucontext.d
/usr/include/d/core/sys/posix/unistd.d
/usr/include/d/core/sys/posix/utime.d
/usr/include/d/core/sys/solaris/dlfcn.d
/usr/include/d/core/sys/solaris/elf.d
/usr/include/d/core/sys/solaris/execinfo.d
/usr/include/d/core/sys/solaris/libelf.d
/usr/include/d/core/sys/solaris/link.d
/usr/include/d/core/sys/solaris/sys/elf.d
/usr/include/d/core/sys/solaris/sys/elf_386.d
/usr/include/d/core/sys/solaris/sys/elf_SPARC.d
/usr/include/d/core/sys/solaris/sys/elf_amd64.d
/usr/include/d/core/sys/solaris/sys/elf_notes.d
/usr/include/d/core/sys/solaris/sys/elftypes.d
/usr/include/d/core/sys/solaris/sys/link.d
/usr/include/d/core/sys/solaris/sys/priocntl.d
/usr/include/d/core/sys/solaris/sys/procset.d
/usr/include/d/core/sys/solaris/sys/types.d
/usr/include/d/core/sys/solaris/time.d
/usr/include/d/core/sys/windows/accctrl.d
/usr/include/d/core/sys/windows/aclapi.d
/usr/include/d/core/sys/windows/aclui.d
/usr/include/d/core/sys/windows/basetsd.d
/usr/include/d/core/sys/windows/basetyps.d
/usr/include/d/core/sys/windows/cderr.d
/usr/include/d/core/sys/windows/cguid.d
/usr/include/d/core/sys/windows/com.d
/usr/include/d/core/sys/windows/comcat.d
/usr/include/d/core/sys/windows/commctrl.d
/usr/include/d/core/sys/windows/commdlg.d
/usr/include/d/core/sys/windows/core.d
/usr/include/d/core/sys/windows/cpl.d
/usr/include/d/core/sys/windows/cplext.d
/usr/include/d/core/sys/windows/custcntl.d
/usr/include/d/core/sys/windows/dbghelp.d
/usr/include/d/core/sys/windows/dbghelp_types.d
/usr/include/d/core/sys/windows/dbt.d
/usr/include/d/core/sys/windows/dde.d
/usr/include/d/core/sys/windows/ddeml.d
/usr/include/d/core/sys/windows/dhcpcsdk.d
/usr/include/d/core/sys/windows/dlgs.d
/usr/include/d/core/sys/windows/dll.d
/usr/include/d/core/sys/windows/docobj.d
/usr/include/d/core/sys/windows/errorrep.d
/usr/include/d/core/sys/windows/exdisp.d
/usr/include/d/core/sys/windows/exdispid.d
/usr/include/d/core/sys/windows/httpext.d
/usr/include/d/core/sys/windows/idispids.d
/usr/include/d/core/sys/windows/imagehlp.d
/usr/include/d/core/sys/windows/imm.d
/usr/include/d/core/sys/windows/intshcut.d
/usr/include/d/core/sys/windows/ipexport.d
/usr/include/d/core/sys/windows/iphlpapi.d
/usr/include/d/core/sys/windows/ipifcons.d
/usr/include/d/core/sys/windows/iprtrmib.d
/usr/include/d/core/sys/windows/iptypes.d
/usr/include/d/core/sys/windows/isguids.d
/usr/include/d/core/sys/windows/lm.d
/usr/include/d/core/sys/windows/lmaccess.d
/usr/include/d/core/sys/windows/lmalert.d
/usr/include/d/core/sys/windows/lmapibuf.d
/usr/include/d/core/sys/windows/lmat.d
/usr/include/d/core/sys/windows/lmaudit.d
/usr/include/d/core/sys/windows/lmbrowsr.d
/usr/include/d/core/sys/windows/lmchdev.d
/usr/include/d/core/sys/windows/lmconfig.d
/usr/include/d/core/sys/windows/lmcons.d
/usr/include/d/core/sys/windows/lmerr.d
/usr/include/d/core/sys/windows/lmerrlog.d
/usr/include/d/core/sys/windows/lmmsg.d
/usr/include/d/core/sys/windows/lmremutl.d
/usr/include/d/core/sys/windows/lmrepl.d
/usr/include/d/core/sys/windows/lmserver.d
/usr/include/d/core/sys/windows/lmshare.d
/usr/include/d/core/sys/windows/lmsname.d
/usr/include/d/core/sys/windows/lmstats.d
/usr/include/d/core/sys/windows/lmsvc.d
/usr/include/d/core/sys/windows/lmuse.d
/usr/include/d/core/sys/windows/lmuseflg.d
/usr/include/d/core/sys/windows/lmwksta.d
/usr/include/d/core/sys/windows/lzexpand.d
/usr/include/d/core/sys/windows/mapi.d
/usr/include/d/core/sys/windows/mciavi.d
/usr/include/d/core/sys/windows/mcx.d
/usr/include/d/core/sys/windows/mgmtapi.d
/usr/include/d/core/sys/windows/mmsystem.d
/usr/include/d/core/sys/windows/msacm.d
/usr/include/d/core/sys/windows/mshtml.d
/usr/include/d/core/sys/windows/mswsock.d
/usr/include/d/core/sys/windows/nb30.d
/usr/include/d/core/sys/windows/nddeapi.d
/usr/include/d/core/sys/windows/nspapi.d
/usr/include/d/core/sys/windows/ntdef.d
/usr/include/d/core/sys/windows/ntdll.d
/usr/include/d/core/sys/windows/ntldap.d
/usr/include/d/core/sys/windows/ntsecapi.d
/usr/include/d/core/sys/windows/ntsecpkg.d
/usr/include/d/core/sys/windows/oaidl.d
/usr/include/d/core/sys/windows/objbase.d
/usr/include/d/core/sys/windows/objfwd.d
/usr/include/d/core/sys/windows/objidl.d
/usr/include/d/core/sys/windows/objsafe.d
/usr/include/d/core/sys/windows/ocidl.d
/usr/include/d/core/sys/windows/odbcinst.d
/usr/include/d/core/sys/windows/ole.d
/usr/include/d/core/sys/windows/ole2.d
/usr/include/d/core/sys/windows/ole2ver.d
/usr/include/d/core/sys/windows/oleacc.d
/usr/include/d/core/sys/windows/oleauto.d
/usr/include/d/core/sys/windows/olectl.d
/usr/include/d/core/sys/windows/olectlid.d
/usr/include/d/core/sys/windows/oledlg.d
/usr/include/d/core/sys/windows/oleidl.d
/usr/include/d/core/sys/windows/pbt.d
/usr/include/d/core/sys/windows/powrprof.d
/usr/include/d/core/sys/windows/prsht.d
/usr/include/d/core/sys/windows/psapi.d
/usr/include/d/core/sys/windows/rapi.d
/usr/include/d/core/sys/windows/ras.d
/usr/include/d/core/sys/windows/rasdlg.d
/usr/include/d/core/sys/windows/raserror.d
/usr/include/d/core/sys/windows/rassapi.d
/usr/include/d/core/sys/windows/reason.d
/usr/include/d/core/sys/windows/regstr.d
/usr/include/d/core/sys/windows/richedit.d
/usr/include/d/core/sys/windows/richole.d
/usr/include/d/core/sys/windows/rpc.d
/usr/include/d/core/sys/windows/rpcdce.d
/usr/include/d/core/sys/windows/rpcdce2.d
/usr/include/d/core/sys/windows/rpcdcep.d
/usr/include/d/core/sys/windows/rpcndr.d
/usr/include/d/core/sys/windows/rpcnsi.d
/usr/include/d/core/sys/windows/rpcnsip.d
/usr/include/d/core/sys/windows/rpcnterr.d
/usr/include/d/core/sys/windows/schannel.d
/usr/include/d/core/sys/windows/secext.d
/usr/include/d/core/sys/windows/security.d
/usr/include/d/core/sys/windows/servprov.d
/usr/include/d/core/sys/windows/setupapi.d
/usr/include/d/core/sys/windows/shellapi.d
/usr/include/d/core/sys/windows/shldisp.d
/usr/include/d/core/sys/windows/shlguid.d
/usr/include/d/core/sys/windows/shlobj.d
/usr/include/d/core/sys/windows/shlwapi.d
/usr/include/d/core/sys/windows/snmp.d
/usr/include/d/core/sys/windows/sql.d
/usr/include/d/core/sys/windows/sqlext.d
/usr/include/d/core/sys/windows/sqltypes.d
/usr/include/d/core/sys/windows/sqlucode.d
/usr/include/d/core/sys/windows/sspi.d
/usr/include/d/core/sys/windows/stacktrace.d
/usr/include/d/core/sys/windows/stat.d
/usr/include/d/core/sys/windows/subauth.d
/usr/include/d/core/sys/windows/threadaux.d
/usr/include/d/core/sys/windows/tlhelp32.d
/usr/include/d/core/sys/windows/tmschema.d
/usr/include/d/core/sys/windows/unknwn.d
/usr/include/d/core/sys/windows/uuid.d
/usr/include/d/core/sys/windows/vfw.d
/usr/include/d/core/sys/windows/w32api.d
/usr/include/d/core/sys/windows/winbase.d
/usr/include/d/core/sys/windows/winber.d
/usr/include/d/core/sys/windows/wincon.d
/usr/include/d/core/sys/windows/wincrypt.d
/usr/include/d/core/sys/windows/windef.d
/usr/include/d/core/sys/windows/windows.d
/usr/include/d/core/sys/windows/winerror.d
/usr/include/d/core/sys/windows/wingdi.d
/usr/include/d/core/sys/windows/winhttp.d
/usr/include/d/core/sys/windows/wininet.d
/usr/include/d/core/sys/windows/winioctl.d
/usr/include/d/core/sys/windows/winldap.d
/usr/include/d/core/sys/windows/winnetwk.d
/usr/include/d/core/sys/windows/winnls.d
/usr/include/d/core/sys/windows/winnt.d
/usr/include/d/core/sys/windows/winperf.d
/usr/include/d/core/sys/windows/winreg.d
/usr/include/d/core/sys/windows/winsock2.d
/usr/include/d/core/sys/windows/winspool.d
/usr/include/d/core/sys/windows/winsvc.d
/usr/include/d/core/sys/windows/winuser.d
/usr/include/d/core/sys/windows/winver.d
/usr/include/d/core/sys/windows/wtsapi32.d
/usr/include/d/core/sys/windows/wtypes.d
/usr/include/d/core/thread.d
/usr/include/d/core/time.d
/usr/include/d/core/vararg.d
/usr/include/d/etc/c/curl.d
/usr/include/d/etc/c/odbc/sql.d
/usr/include/d/etc/c/odbc/sqlext.d
/usr/include/d/etc/c/odbc/sqltypes.d
/usr/include/d/etc/c/odbc/sqlucode.d
/usr/include/d/etc/c/sqlite3.d
/usr/include/d/etc/c/zlib.d
/usr/include/d/etc/linux/memoryerror.d
/usr/include/d/ldc/asan.d
/usr/include/d/ldc/attributes.d
/usr/include/d/ldc/dcompute.d
/usr/include/d/ldc/eh_msvc.d
/usr/include/d/ldc/gccbuiltins_aarch64.di
/usr/include/d/ldc/gccbuiltins_arm.di
/usr/include/d/ldc/gccbuiltins_mips.di
/usr/include/d/ldc/gccbuiltins_ppc.di
/usr/include/d/ldc/gccbuiltins_s390.di
/usr/include/d/ldc/gccbuiltins_x86.di
/usr/include/d/ldc/internal/vararg.di
/usr/include/d/ldc/intrinsics.di
/usr/include/d/ldc/libfuzzer.di
/usr/include/d/ldc/llvmasm.di
/usr/include/d/ldc/profile.di
/usr/include/d/ldc/sanitizer_common.d
/usr/include/d/ldc/sanitizers_optionally_linked.d
/usr/include/d/ldc/simd.di
/usr/include/d/object.d
/usr/include/d/std/algorithm/comparison.d
/usr/include/d/std/algorithm/internal.d
/usr/include/d/std/algorithm/iteration.d
/usr/include/d/std/algorithm/mutation.d
/usr/include/d/std/algorithm/package.d
/usr/include/d/std/algorithm/searching.d
/usr/include/d/std/algorithm/setops.d
/usr/include/d/std/algorithm/sorting.d
/usr/include/d/std/array.d
/usr/include/d/std/ascii.d
/usr/include/d/std/base64.d
/usr/include/d/std/bigint.d
/usr/include/d/std/bitmanip.d
/usr/include/d/std/compiler.d
/usr/include/d/std/complex.d
/usr/include/d/std/concurrency.d
/usr/include/d/std/container/array.d
/usr/include/d/std/container/binaryheap.d
/usr/include/d/std/container/dlist.d
/usr/include/d/std/container/package.d
/usr/include/d/std/container/rbtree.d
/usr/include/d/std/container/slist.d
/usr/include/d/std/container/util.d
/usr/include/d/std/conv.d
/usr/include/d/std/csv.d
/usr/include/d/std/datetime/date.d
/usr/include/d/std/datetime/interval.d
/usr/include/d/std/datetime/package.d
/usr/include/d/std/datetime/stopwatch.d
/usr/include/d/std/datetime/systime.d
/usr/include/d/std/datetime/timezone.d
/usr/include/d/std/demangle.d
/usr/include/d/std/digest/crc.d
/usr/include/d/std/digest/digest.d
/usr/include/d/std/digest/hmac.d
/usr/include/d/std/digest/md.d
/usr/include/d/std/digest/murmurhash.d
/usr/include/d/std/digest/package.d
/usr/include/d/std/digest/ripemd.d
/usr/include/d/std/digest/sha.d
/usr/include/d/std/encoding.d
/usr/include/d/std/exception.d
/usr/include/d/std/experimental/all.d
/usr/include/d/std/experimental/allocator/building_blocks/affix_allocator.d
/usr/include/d/std/experimental/allocator/building_blocks/aligned_block_list.d
/usr/include/d/std/experimental/allocator/building_blocks/allocator_list.d
/usr/include/d/std/experimental/allocator/building_blocks/ascending_page_allocator.d
/usr/include/d/std/experimental/allocator/building_blocks/bitmapped_block.d
/usr/include/d/std/experimental/allocator/building_blocks/bucketizer.d
/usr/include/d/std/experimental/allocator/building_blocks/fallback_allocator.d
/usr/include/d/std/experimental/allocator/building_blocks/free_list.d
/usr/include/d/std/experimental/allocator/building_blocks/free_tree.d
/usr/include/d/std/experimental/allocator/building_blocks/kernighan_ritchie.d
/usr/include/d/std/experimental/allocator/building_blocks/null_allocator.d
/usr/include/d/std/experimental/allocator/building_blocks/package.d
/usr/include/d/std/experimental/allocator/building_blocks/quantizer.d
/usr/include/d/std/experimental/allocator/building_blocks/region.d
/usr/include/d/std/experimental/allocator/building_blocks/scoped_allocator.d
/usr/include/d/std/experimental/allocator/building_blocks/segregator.d
/usr/include/d/std/experimental/allocator/building_blocks/stats_collector.d
/usr/include/d/std/experimental/allocator/common.d
/usr/include/d/std/experimental/allocator/gc_allocator.d
/usr/include/d/std/experimental/allocator/mallocator.d
/usr/include/d/std/experimental/allocator/mmap_allocator.d
/usr/include/d/std/experimental/allocator/package.d
/usr/include/d/std/experimental/allocator/showcase.d
/usr/include/d/std/experimental/allocator/typed.d
/usr/include/d/std/experimental/checkedint.d
/usr/include/d/std/experimental/logger/core.d
/usr/include/d/std/experimental/logger/filelogger.d
/usr/include/d/std/experimental/logger/multilogger.d
/usr/include/d/std/experimental/logger/nulllogger.d
/usr/include/d/std/experimental/logger/package.d
/usr/include/d/std/experimental/typecons.d
/usr/include/d/std/file.d
/usr/include/d/std/format.d
/usr/include/d/std/functional.d
/usr/include/d/std/getopt.d
/usr/include/d/std/internal/attributes.d
/usr/include/d/std/internal/cstring.d
/usr/include/d/std/internal/digest/sha_SSSE3.d
/usr/include/d/std/internal/math/biguintarm.d
/usr/include/d/std/internal/math/biguintcore.d
/usr/include/d/std/internal/math/biguintnoasm.d
/usr/include/d/std/internal/math/biguintx86.d
/usr/include/d/std/internal/math/errorfunction.d
/usr/include/d/std/internal/math/gammafunction.d
/usr/include/d/std/internal/memory.d
/usr/include/d/std/internal/scopebuffer.d
/usr/include/d/std/internal/test/dummyrange.d
/usr/include/d/std/internal/test/range.d
/usr/include/d/std/internal/test/uda.d
/usr/include/d/std/internal/unicode_comp.d
/usr/include/d/std/internal/unicode_decomp.d
/usr/include/d/std/internal/unicode_grapheme.d
/usr/include/d/std/internal/unicode_norm.d
/usr/include/d/std/internal/unicode_tables.d
/usr/include/d/std/internal/windows/advapi32.d
/usr/include/d/std/json.d
/usr/include/d/std/math.d
/usr/include/d/std/mathspecial.d
/usr/include/d/std/meta.d
/usr/include/d/std/mmfile.d
/usr/include/d/std/net/curl.d
/usr/include/d/std/net/isemail.d
/usr/include/d/std/numeric.d
/usr/include/d/std/outbuffer.d
/usr/include/d/std/package.d
/usr/include/d/std/parallelism.d
/usr/include/d/std/path.d
/usr/include/d/std/process.d
/usr/include/d/std/random.d
/usr/include/d/std/range/interfaces.d
/usr/include/d/std/range/package.d
/usr/include/d/std/range/primitives.d
/usr/include/d/std/regex/internal/backtracking.d
/usr/include/d/std/regex/internal/generator.d
/usr/include/d/std/regex/internal/ir.d
/usr/include/d/std/regex/internal/kickstart.d
/usr/include/d/std/regex/internal/parser.d
/usr/include/d/std/regex/internal/tests.d
/usr/include/d/std/regex/internal/tests2.d
/usr/include/d/std/regex/internal/thompson.d
/usr/include/d/std/regex/package.d
/usr/include/d/std/signals.d
/usr/include/d/std/socket.d
/usr/include/d/std/stdint.d
/usr/include/d/std/stdio.d
/usr/include/d/std/string.d
/usr/include/d/std/system.d
/usr/include/d/std/traits.d
/usr/include/d/std/typecons.d
/usr/include/d/std/typetuple.d
/usr/include/d/std/uni.d
/usr/include/d/std/uri.d
/usr/include/d/std/utf.d
/usr/include/d/std/uuid.d
/usr/include/d/std/variant.d
/usr/include/d/std/windows/charset.d
/usr/include/d/std/windows/registry.d
/usr/include/d/std/windows/syserror.d
/usr/include/d/std/xml.d
/usr/include/d/std/zip.d
/usr/include/d/std/zlib.d
/usr/lib64/libdruntime-ldc-debug-shared.so
/usr/lib64/libdruntime-ldc-shared.so
/usr/lib64/libphobos2-ldc-debug-shared.so
/usr/lib64/libphobos2-ldc-shared.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libdruntime-ldc-debug-shared.so.2.0.87
/usr/lib64/libdruntime-ldc-debug-shared.so.87
/usr/lib64/libdruntime-ldc-shared.so.2.0.87
/usr/lib64/libdruntime-ldc-shared.so.87
/usr/lib64/libphobos2-ldc-debug-shared.so.2.0.87
/usr/lib64/libphobos2-ldc-debug-shared.so.87
/usr/lib64/libphobos2-ldc-shared.so.2.0.87
/usr/lib64/libphobos2-ldc-shared.so.87

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ldc/LICENSE
/usr/share/package-licenses/ldc/runtime_druntime_LICENSE.txt
/usr/share/package-licenses/ldc/runtime_phobos_LICENSE_1_0.txt
