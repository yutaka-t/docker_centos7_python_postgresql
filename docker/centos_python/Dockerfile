# ベース指定
FROM centos:centos7
RUN yum install -y which postgresql-devel

#python
ARG python_ver=3.9
ARG pyton_detailed_ver=3.9.6
RUN yum groupinstall -y 'development tools' \
    && yum -y install bzip2-devel gdbm-devel libffi-devel \
    libuuid-devel ncurses-devel openssl-devel readline-devel \
    sqlite-devel tk-devel wget xz-devel zlib-devel
WORKDIR /tmp
RUN wget https://www.python.org/ftp/python/${pyton_detailed_ver}/Python-${pyton_detailed_ver}.tgz
RUN tar xvfz Python-${pyton_detailed_ver}.tgz
WORKDIR /tmp/Python-${pyton_detailed_ver}
RUN ./configure --enable-optimizations
RUN make altinstall
WORKDIR /tmp
RUN rm -fr ./Python-${pyton_detailed_ver}*

# python ライブラリ追加
RUN pip${python_ver} install --upgrade pip
RUN pip${python_ver} install psycopg2 numpy pandas 

# LANG設定
# Dockerで公式のCentOS 7をデフォルトで使用した場合などで、環境変数LANGが未定義となっている為
RUN echo 'export LANG=en_US.UFT-8' >> /root/.bashrc
RUN echo 'export PATH=/usr/pgsql-12/bin:$PATH' >> /root/.bashrc

# インストールしたPythonにパスを通す
# ここを有効にするとyumが使えなくなる。(yumはpython2で作成されている為)
# 有効にしない場合は、python3.9 pip2.9 のようにバージョンを付けて呼び出す事
# RUN ln -sf /usr/local/bin/python${python_ver} /usr/bin/python
# RUN ln -sf /usr/local/bin/pip${python_ver} /usr/bin/pip
# RUN echo 'LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/python${python_ver}/lib"' >> ~/.bashrc
# RUN echo 'PATH="$PATH:/usr/local/python${python_ver}/bin"' >> ~/.bashrc

