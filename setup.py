from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
 
import numpy
import sys

#Se GSL Library
#if sys.platform == "win32":
#	include_gsl_dir = sys.exec_prefix.lower().split("anaconda")[0]+"anaconda\\gsl\\include"
#	lib_gsl_dir = sys.exec_prefix.lower().split("anaconda")[0]+"anaconda\\gsl\\lib"
#else:
#	include_gsl_dir = sys.exec_prefix+"\\include"
#	lib_gsl_dir = sys.exec_prefix+"\\lib"
  
include_gsl_dir = "/usr/local/include/"
lib_gsl_dir = "/usr/local/lib/"
     
ext = Extension("topicmodels.samplers.samplers_lda", ["topicmodels/samplers/samplers_lda.pyx"],
   include_dirs=[numpy.get_include(), 
                 include_gsl_dir],
   library_dirs=[lib_gsl_dir],
   libraries=["gsl","gslcblas","m"]
)

# ext = Extension("topicmodels.samplers.samplers_lda", ["topicmodels/samplers/samplers_lda.pyx"],
#     include_dirs=[numpy.get_include()]
# )
 
setup(name = "topicmodels.samplers.samplers_lda",
	ext_modules=[ext],
    cmdclass = {'build_ext': build_ext})
