import requests

class Promdata:
    """
    A class that retrieves data from prometheus
    ...
    Atributes
    -----------
    type: str
        Default "https://" unless disable_https is called.
    dns: str
        dns name to be in the url.
    api: str
        Part of the url that comes after the dns (default "/api/v1/query?query=").
    url: str
        Composed of the type, dns, and api.

    Methods
    --------
    disabled_https(self):
        Changes the type to "http://" and changed the url accordingly.

    wallclock(self, period, offset=""):
        Retrieves and returns the total wallclock time queried from prometheus using the url.

    gpu(self, period, requested=False, offset=""):
        Retrieves and returns the total or requested gpu usage queried from prometheus using the url.

    cpu(self, period, requested=False, offset=""):
        Retrieved and returns the total or requested cpu usage queried from prometheus using the url.

    memory(self, period, offset=""):
        Retrieves and returns the total memory usage queried from prometheus using the url.

    network(self, period, offset="", kind="received")
        retrieves and returns the total network bytes receieved or transmitted from prometheus using the url.

    """

    def __init__(self, dns_, api_="/api/v1/query?query="):
        """
        Parameters
        ----------
        dns_ : str
            dns name to be put in the url.
        api_ : str
            api to follow the dns in the url, comes before the query.
        """

        self.type = "https://"
        self.dns = dns_
        self.api = api_
        self.url = self.type + self.dns + self.api

    def disable_https(self):
        """Changes the type to "http:// and the url accordingly."""

        self.type = "http://"
        self.url = self.type + self.dns + self.api

    def wallclock(self, period, offset=""):
        """Retrieves and returns the total wallclock time queried from prometheus using the url.

        Parameters
        ----------
        period : str
            Range vector over which the data is collected.
        offset : str
            How far in the past to retrieve the data from, default is an empty string (present).
        """

        query = 'sum(sum_over_time(node_namespace_pod:kube_pod_info:[' + period + ']'
        if offset:
            query = query + ' offset ' + offset
        query += ')) by (namespace)'
        return requests.get(self.url + query).json()

    def gpu(self, period, requested=False, offset=""):
        """Retrieves and returns the total requested gpus or the total gpu usage over the time period indicated.

        Parameters
        -----------
        period: str
            Range vector over which the data is collected.
        requested: bool
            Default is false, if true returns the total gpus requested as opposed to the total usage.
        offset: str
            How far in the past to retrieve the data from, default is an empty string (present).
        """

        if requested:
            query = 'sum(sum_over_time(pod_gpus[' + period + ':1s]'
            if offset:
                query = query + ' offset ' + offset
            query += ')) by (namespace_name)'
            return requests.get(self.url + query).json()
        query = 'sum_over_time(namespace_gpu_utilization[' + period + ':1s]'
        if offset:
            query = query + ' offset ' + offset
        query += ')'
        return requests.get(self.url + query).json()

    def cpu(self, period, requested=False, offset=""):
        """retrieves and returns the total cpus used or requested over the specified time period.

        Parameters
        -----------
        period: str
            Range vector over which the data is collected.
        requested: bool
            Default is false, if true returns the total cpus requested as opposed to the total usage.
        offset: str
            How far in the past to retrieve the data from, default is an empty string (present).
        """

        if requested:
            query = 'sum(sum_over_time(kube_pod_container_resource_requests_cpu_cores{container!~\"\"}[' + period + ':1s]'
            if offset:
                query = query + ' offset ' + offset
            query += ')) by (namespace)'
            return requests.get(self.url + query).json()
        query = 'sum(delta(container_cpu_usage_seconds_total{container!~\"\"}[' + period + ':1m]'
        if offset:
            query = query + ' offset ' + offset
        query += ')) by (namespace)'
        return requests.get(self.url + query).json()

    def memory(self, period, offset=""):
        """returns the total memory usage over the indicated period.

        Parameters
        -----------
        period: str
            Range vector over which the data is collected.
        offset: str
            How far in the past to retrieve the data from, default is empty string (present).
        """

        query = 'sum(sum_over_time(namespace:container_memory_usage_bytes:sum[' + period + ':1s]'
        if offset:
            query = query + ' offset ' + offset
        query += ')) by (namespace)'
        return requests.get(self.url + query).json()

    def network(self, period, offset="", kind="received"):
        """returns the total received or transmitted network over the indicated period.

        Parameters
        ----------
        period: str
            Range vector over which the data is collected
        offset: str
            how far in the past to retrieve the data from, default is empty string (present)
            *our experiece shows it is likely to fail if an offset is included*
        kind: str
            default is "received", and returns the total received network. If "transmit" is passed in, the total transmitted network is returned

        """

        if kind == "transmit":
            query = 'sum(delta(container_network_transmit_bytes_total{container!~""}[' + period + ':5m]'
            if offset:
                query = query + ' offset ' + offset
            query += ')) by (namespace)'

        else:
            query = 'sum(delta(container_network_receive_bytes_total{container!~""}[' + period + ':1m]'
            if offset:
                query = query + ' offset ' + offset
            query += ')) by (namespace)'

        return requests.get(self.url + query).json()
