import requests

def walltime(dict_, sort_, unit_="", reverse=False, all=False):
    """Displays the total wallclock time for each namespace in an organized way.

    Parameters
    -----------
    dict_ : json data
        json data to be passed in and parsed.
    sort_ : str
        either "0" to sort alphabetically, or "1" to sort numerically in descending order.
    unit_ : str
        unit by which to convert the data, if empty string is passed in, data is automatically converted to the unit that is best fit.
    reverse : bool
        Default false, if true the sorting is reversed (ascending order or starting the alphabet backwards)
    all : bool
        By default namespaces whose corresponding values are zero are not displayed. If all is passed in as true, all namespaces and their values are displayed.

    """
    values = []
    namespace = []
    name_n_val = []
    dict = dict_["data"]["result"]

    for i in dict:
        namespace.extend(list(list(i.values())[0].values()))
        values.append(list(i.values())[1])

    val = []
    for i in values:
        val.append(float(i[1]))

    div = 1
    unit = unit_
    if unit:
        if unit == "s":
            div = 1
        elif unit == "Ys":
            div = 10**24
        elif unit == "Zs":
            div = 10**21
        elif unit == "Es":
            div = 10**18
        elif unit == "Ps":
            div = 10**15
        elif unit == "Ts":
            div = 10**12
        elif unit == "Gs":
            div = 10**9
        elif unit == "Ms":
            div = 10**6
        elif unit == "ks":
            div = 10**3
    else:
        unit = "s"
        maximum = max(val)
        if maximum/10**24 >= 1000 and maximum/10**24 <= 9999999.9:
            unit = "Ys"
            div = 10**24
        elif maximum/10**21 >= 1000 and maximum/10**21 <= 9999999.9:
            unit = "Zs"
            div = 10**21
        elif maximum/10**18 >= 1000 and maximum/10**18 <= 9999999.9:
            unit = "Es"
            div = 10**18
        elif maximum/10**15 >= 1000 and maximum/10**15 <= 9999999.9:
            unit = "Ps"
            div = 10**15
        elif maximum/10**12 >= 1000 and maximum/10**12 <= 9999999.9:
            unit = "Ts"
            div = 10**12
        elif maximum/10**9 >= 1000 and maximum/10**9 <= 9999999.9:
            unit = "Gs"
            div = 10**9
        elif maximum/10**6 >= 1000 and maximum/10**6 <= 9999999.9:
            unit = "Ms"
            div = 10**6
        elif maximum/10**3 >= 1000 and maximum/10**3 <= 9999999.9:
            unit = "ks"
            div = 10**3

    final_val = []
    for v in val:
        #v = round(v/div, 1)
        v = v/div
        final_val.append(v)

    for i in range(len(namespace)):
        if all:
            name_n_val.append((namespace[i], final_val[i]))
        else:
            if final_val[i] != 0:
                name_n_val.append((namespace[i], final_val[i]))

    def sorter(e, sortby=0):
        if sort_:
            sortby = int(sort_)
        return e[sortby]

    reverse_bool = False
    if reverse:
        reverse_bool = True

    if sort_ == "1":
        reverse_bool = not reverse_bool

    name_n_val.sort(key=sorter, reverse=reverse_bool)

    header = [("namespace:", "wallclock time: (" + unit + ")"), ("------------", "---------------")]

    for h in header:
        format = "%-40s %20s"
        n = format%(h)
        print(n)

    for name in name_n_val:
        format = "%-40s %20s"
        n = format%(name)
        print(n)


def gpu(dict_, sort_, unit_="", reverse=False, all=False):
    """Displays the total gpu usage or gpus requested for each namespace in an organized way.

    Parameters
    -----------
    dict_ : json data
        json data to be passed in and parsed.
    sort_ : str
        either "0" to sort alphabetically, or "1" to sort numerically in descending order.
    unit_ : str
        unit by which to convert the data, if empty string is passed in, data is automatically converted to the unit that is best fit.
    reverse : bool
        Default false, if true the sorting is reversed (ascending order or starting the alphabet backwards)
    all : bool
        By default namespaces whose corresponding values are zero are not displayed. If all is passed in as true, all namespaces and their values are displayed.

    """
    g_namespace = []
    g_values = []
    name_n_val = []
    dict = dict_["data"]["result"]

    for i in dict:
        g_namespace.extend(list(list(i.values())[0].values()))
        g_values.append(list(i.values())[1])


    val = []
    for i in g_values:
        val.append(float(i[1]))

    div = 1
    unit = unit_
    if unit:
        if unit == "s":
            div = 1
        elif unit == "Ys":
            div = 10**24
        elif unit == "Zs":
            div = 10**21
        elif unit == "Es":
            div = 10**18
        elif unit == "Ps":
            div = 10**15
        elif unit == "Ts":
            div = 10**12
        elif unit == "Gs":
            div = 10**9
        elif unit == "Ms":
            div = 10**6
        elif unit == "ks":
            div = 10**3
    else:
        unit = "s"
        maximum = max(val)
        if maximum/10**24 >= 1000 and maximum/10**24 <= 9999999.9:
            unit = "Ys"
            div = 10**24
        elif maximum/10**21 >= 1000 and maximum/10**21 <= 9999999.9:
            unit = "Zs"
            div = 10**21
        elif maximum/10**18 >= 1000 and maximum/10**18 <= 9999999.9:
            unit = "Es"
            div = 10**18
        elif maximum/10**15 >= 1000 and maximum/10**15 <= 9999999.9:
            unit = "Ps"
            div = 10**15
        elif maximum/10**12 >= 1000 and maximum/10**12 <= 9999999.9:
            unit = "Ts"
            div = 10**12
        elif maximum/10**9 >= 1000 and maximum/10**9 <= 9999999.9:
            unit = "Gs"
            div = 10**9
        elif maximum/10**6 >= 1000 and maximum/10**6 <= 9999999.9:
            unit = "Ms"
            div = 10**6
        elif maximum/10**3 >= 1000 and maximum/10**3 <= 9999999.9:
            unit = "ks"
            div = 10**3

    final_val = []
    for v in val:
        v = round(v/div, 1)
        final_val.append(v)

    for i in range(len(g_namespace)):
        if all:
            name_n_val.append((g_namespace[i], final_val[i]))
        else:
            if final_val[i] != 0:
                name_n_val.append((g_namespace[i], final_val[i]))


    def sorter(e, sortby=0):
        if sort_:
            sortby = int(sort_)
        return e[sortby]

    reverse_bool = False
    if reverse:
        reverse_bool = True

    if sort_ == "1":
        reverse_bool = not reverse_bool

    name_n_val.sort(key=sorter, reverse=reverse_bool)

    header = [("namespace:", "gpu: (" + unit + ")"), ("------------", "------------")]

    for h in header:
        format = "%-40s %20s"
        n = format%(h)
        print(n)

    for name in name_n_val:
        format = "%-40s %20s"
        n = format%(name)
        print(n)



def cpu(dict_, sort_, unit_="", reverse=False, all=False):
    """Displays the total cpu usage or cpus requested for each namespace in an organized way.

    Parameters
    -----------
    dict_ : json data
        json data to be passed in and parsed.
    sort_ : str
        either "0" to sort alphabetically, or "1" to sort numerically in descending order.
    unit_ : str
        unit by which to convert the data, if empty string is passed in, data is automatically converted to the unit that is best fit.
    reverse : bool
        Default false, if true the sorting is reversed (ascending order or starting the alphabet backwards)
    all : bool
        By default namespaces whose corresponding values are zero are not displayed. If all is passed in as true, all namespaces and their values are displayed.

    """
    c_namespace = []
    c_values = []
    name_n_val = []
    dict = dict_["data"]["result"]

    for i in dict:
        c_namespace.extend(list(list(i.values())[0].values()))
        c_values.append(list(i.values())[1])

    val = []
    for i in c_values:
        val.append(float(i[1]))

    div = 1
    unit = unit_
    if unit:
        if unit == "s":
            div = 1
        elif unit == "Ys":
            div = 10**24
        elif unit == "Zs":
            div = 10**21
        elif unit == "Es":
            div = 10**18
        elif unit == "Ps":
            div = 10**15
        elif unit == "Ts":
            div = 10**12
        elif unit == "Gs":
            div = 10**9
        elif unit == "Ms":
            div = 10**6
        elif unit == "ks":
            div = 10**3
    else:
        unit = "s"
        maximum = max(val)
        if maximum/10**24 >= 1000 and maximum/10**24 <= 9999999.9:
            unit = "Ys"
            div = 10**24
        elif maximum/10**21 >= 1000 and maximum/10**21 <= 9999999.9:
            unit = "Zs"
            div = 10**21
        elif maximum/10**18 >= 1000 and maximum/10**18 <= 9999999.9:
            unit = "Es"
            div = 10**18
        elif maximum/10**15 >= 1000 and maximum/10**15 <= 9999999.9:
            unit = "Ps"
            div = 10**15
        elif maximum/10**12 >= 1000 and maximum/10**12 <= 9999999.9:
            unit = "Ts"
            div = 10**12
        elif maximum/10**9 >= 1000 and maximum/10**9 <= 9999999.9:
            unit = "Gs"
            div = 10**9
        elif maximum/10**6 >= 1000 and maximum/10**6 <= 9999999.9:
            unit = "Ms"
            div = 10**6
        elif maximum/10**3 >= 1000 and maximum/10**3 <= 9999999.9:
            unit = "ks"
            div = 10**3

    final_val = []
    for v in val:
        v = round(v/div, 1)
        final_val.append(v)


    for i in range(len(c_namespace)):
        if all:
            name_n_val.append((c_namespace[i], final_val[i]))
        else:
            if final_val[i] != 0:
                name_n_val.append((c_namespace[i], final_val[i]))


    def sorter(e, sortby=0):
        if sort_:
            sortby = int(sort_)
        return e[sortby]

    reverse_bool = False
    if reverse:
        reverse_bool = True

    if sort_ == "1":
        reverse_bool = not reverse_bool

    name_n_val.sort(key=sorter, reverse=reverse_bool)

    header = [("namespace:", "cpu: (" + unit + ")"), ("-------------", "-------------")]

    for h in header:
        format = "%-40s %20s"
        n = format%(h)
        print(n)

    for name in name_n_val:
        format = "%-40s %20s"
        n = format%(name)
        print(n)



def memory(dict_, sort_, unit_="", reverse=False, all=False):
    """Displays the total memory usage for each namespace in an organized way.

    Parameters
    -----------
    dict_ : json data
        json data to be passed in and parsed.
    sort_ : str
        either "0" to sort alphabetically, or "1" to sort numerically in descending order.
    unit_ : str
        unit by which to convert the data, if empty string is passed in, data is automatically converted to the unit that is best fit.
    reverse : bool
        Default false, if true the sorting is reversed (ascending order or starting the alphabet backwards)
    all : bool
        By default namespaces whose corresponding values are zero are not displayed. If all is passed in as true, all namespaces and their values are displayed.

    """
    m_namespace = []
    m_values = []
    name_n_val = []
    dict = dict_["data"]["result"]

    for i in dict:
        m_namespace.extend(list(list(i.values())[0].values()))
        m_values.append(list(i.values())[1])

    val = []
    for i in m_values:
        val.append(float(i[1]))

    div = 1
    unit = unit_
    if unit:
        if unit == "s":
            div = 1
        elif unit == "Ys":
            div = 10**24
        elif unit == "Zs":
            div = 10**21
        elif unit == "Es":
            div = 10**18
        elif unit == "Ps":
            div = 10**15
        elif unit == "Ts":
            div = 10**12
        elif unit == "Gs":
            div = 10**9
        elif unit == "Ms":
            div = 10**6
        elif unit == "ks":
            div = 10**3
    else:
        unit = "s"
        maximum = max(val)
        if maximum/10**24 >= 1000 and maximum/10**24 <= 9999999.9:
            unit = "Ys"
            div = 10**24
        elif maximum/10**21 >= 1000 and maximum/10**21 <= 9999999.9:
            unit = "Zs"
            div = 10**21
        elif maximum/10**18 >= 1000 and maximum/10**18 <= 9999999.9:
            unit = "Es"
            div = 10**18
        elif maximum/10**15 >= 1000 and maximum/10**15 <= 9999999.9:
            unit = "Ps"
            div = 10**15
        elif maximum/10**12 >= 1000 and maximum/10**12 <= 9999999.9:
            unit = "Ts"
            div = 10**12
        elif maximum/10**9 >= 1000 and maximum/10**9 <= 9999999.9:
            unit = "Gs"
            div = 10**9
        elif maximum/10**6 >= 1000 and maximum/10**6 <= 9999999.9:
            unit = "Ms"
            div = 10**6
        elif maximum/10**3 >= 1000 and maximum/10**3 <= 9999999.9:
            unit = "ks"
            div = 10**3

    final_val = []
    for v in val:
        v = round(v/div, 1)
        final_val.append(v)


    for i in range(len(m_namespace)):
        if all:
            name_n_val.append((m_namespace[i], final_val[i]))
        else:
            if final_val[i] != 0:
                name_n_val.append((m_namespace[i], final_val[i]))

    def sorter(e, sortby=0):
        if sort_:
            sortby = int(sort_)
        return e[sortby]

    reverse_bool = False
    if reverse:
        reverse_bool = True

    if sort_ == "1":
        reverse_bool = not reverse_bool

    name_n_val.sort(key=sorter, reverse=reverse_bool)

    header = [("namespace:", "memory: (" + unit + ")"), ("------------", "------------")]

    for h in header:
        format = "%-40s %20s"
        n = format%(h)
        print(n)

    for name in name_n_val:
        format = "%-40s %20s"
        n = format%(name)
        print(n)

def network(dict_, sort_, unit_="", reverse=False, all=False):
    """Displays the total network received or transmitted for each namespace in an organized way.

    Parameters
    -----------
    dict_ : json data
        json data to be passed in and parsed.
    sort_ : str
        either "0" to sort alphabetically, or "1" to sort numerically in descending order.
    unit_ : str
        unit by which to convert the data, if empty string is passed in, data is automatically converted to the unit that is best fit.
    reverse : bool
        Default false, if true the sorting is reversed (ascending order or starting the alphabet backwards)
    all : bool
        By default namespaces whose corresponding values are zero are not displayed. If all is passed in as true, all namespaces and their values are displayed.

    """
    n_namespace = []
    n_values = []
    name_n_val = []
    dict = dict_["data"]["result"]

    for i in dict:
        n_namespace.extend(list(list(i.values())[0].values()))
        n_values.append(list(i.values())[1])

    val = []
    for i in n_values:
        val.append(float(i[1]))

    div = 1
    unit = unit_
    if unit:
        if unit == "s":
            div = 1
        elif unit == "Ys":
            div = 10**24
        elif unit == "Zs":
            div = 10**21
        elif unit == "Es":
            div = 10**18
        elif unit == "Ps":
            div = 10**15
        elif unit == "Ts":
            div = 10**12
        elif unit == "Gs":
            div = 10**9
        elif unit == "Ms":
            div = 10**6
        elif unit == "ks":
            div = 10**3
    else:
        unit = "s"
        maximum = max(val)
        if maximum/10**24 >= 1000 and maximum/10**24 <= 9999999.9:
            unit = "Ys"
            div = 10**24
        elif maximum/10**21 >= 1000 and maximum/10**21 <= 9999999.9:
            unit = "Zs"
            div = 10**21
        elif maximum/10**18 >= 1000 and maximum/10**18 <= 9999999.9:
            unit = "Es"
            div = 10**18
        elif maximum/10**15 >= 1000 and maximum/10**15 <= 9999999.9:
            unit = "Ps"
            div = 10**15
        elif maximum/10**12 >= 1000 and maximum/10**12 <= 9999999.9:
            unit = "Ts"
            div = 10**12
        elif maximum/10**9 >= 1000 and maximum/10**9 <= 9999999.9:
            unit = "Gs"
            div = 10**9
        elif maximum/10**6 >= 1000 and maximum/10**6 <= 9999999.9:
            unit = "Ms"
            div = 10**6
        elif maximum/10**3 >= 1000 and maximum/10**3 <= 9999999.9:
            unit = "ks"
            div = 10**3

    final_val = []
    for v in val:
        v = round(v/div, 1)
        final_val.append(v)


    for i in range(len(n_namespace)):
        if all:
            name_n_val.append((n_namespace[i], final_val[i]))
        else:
            if final_val[i] != 0:
                name_n_val.append((n_namespace[i], final_val[i]))

    def sorter(e, sortby=0):
        if sort_:
            sortby = int(sort_)
        return e[sortby]

    reverse_bool = False
    if reverse:
        reverse_bool = True

    if sort_ == "1":
        reverse_bool = not reverse_bool

    name_n_val.sort(key=sorter, reverse=reverse_bool)

    header = [("namespace:", "network: (" + unit + ")"), ("------------", "------------")]

    for h in header:
        format = "%-40s %20s"
        n = format%(h)
        print(n)

    for name in name_n_val:
        format = "%-40s %20s"
        n = format%(name)
        print(n)
