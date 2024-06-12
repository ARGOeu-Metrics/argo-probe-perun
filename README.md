# argo-probe-perun

The simple probe that checks if Perun service is up and running. It takes three required arguments: hostname, certificate file and certificate key file.

## Usage

Example execution of the probe:

```
$ /usr/libexec/argo/probes/perun/check_perun -H "perun.egi.eu" -C /etc/nagios/globus/robotcert.pem -K /etc/nagios/globus/robotkey.pem
OK - Version of PerunDB: 3.2.20
```
