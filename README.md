# Testing integrating Rust with Python

Based off a [Red hat blog](https://developers.redhat.com/blog/2017/11/16/speed-python-using-rust#create_a_new_crate).

## Setup

This work was performed on macOS 11.4 and specific `rustflags` have been set in `pyext-myrustlib/.cargo/config` for building on macOS.

Create a venv with requirements.

```bash
python -m venv myenv

source myenv/bin/activate

(myenv) pip install -r requirements.txt
```

## Building cython double implementation

Now added a quick cythonized version of double. You can compile this locally by doing:

```bash
python setup.py build_ext --inplace
```