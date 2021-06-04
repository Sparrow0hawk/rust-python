# shell script for creating rustlib and moving it to correct place 
# enter venv
source myenv/bin/activate

# enter rust module and build it
cd pyext-myrustlib
cargo build --release

# navigate back up to main repo directory
cd ..

# create a .so file from .dylib and move it to top level
cp pyext-myrustlib/target/release/libmyrustlib.dylib myrustlib.so

# run the test file
python test-double.py