#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
<<<<<<< HEAD
	long int size = PyList_Size(p);
	int i;
	PyListObject *obj - (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i]->tp_name);
}

=======
    long int size = PyList_Size(p);
    int i;
    PyListObject *obj = (PyListObject *)p;

    printf("[*] Size of the Python List = %li\n", size);
    printf("[*] Allocated = %li\n", obj->allocated);
    for (i = 0; i < size; i++)
        printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
>>>>>>> 8b772219eda3370c3e4f7c83fbc039c3b91df9e8
