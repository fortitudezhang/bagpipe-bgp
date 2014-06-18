# vim: tabstop=4 shiftwidth=4 softtabstop=4
# encoding: utf-8

# Copyright 2014 Orange
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#    http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class VPNNotFound(Exception):
    def __init__(self, vrfId):
        self.message = "VRF %(vrfId)s could not be found" % locals()
     
    def __str__(self):
        return repr(self.message)
       
class MalformedIPAddress(Exception):
    def __init__(self, ipAddress):
        self.message = "Address %(ipAddress)s does not look like a valid IP address" % locals()
     
    def __str__(self):
        return repr(self.message)
    
class OVSBridgeNotFound(Exception):
    def __init__(self, bridge):
        self.message = "OVS bridge {%(bridge)s} doesn't exist, specify ovs_bridge in bgp.conf, check that bridge is created, e.g. can be created on Debian using Linux network configuration file {/etc/network/interfaces} as follow:\n\n\
                        allow-ovs ovsbr0\n\
                        iface ovsbr0 inet static\n\
                        ovs_type OVSBridge\n\
                        ovs_ports ethX\n\
                        address <host IP>\n\
                        netmask 255.255.255.0\n\
                        post-up ip route add <network IP>/24 nexthop via <gateway IP> dev ovsbr0\n\n\
                        allow-ovsbr0 ethX\n\
                        iface ethX inet manual\n\
                        ovs_bridge ovsbr0\n\
                        ovs_type OVSPort\n\n" % locals()
     
    def __str__(self):
        return str(self.message)
    
class OVSBridgePortNotFound(Exception):
    def __init__(self, interface, bridge):
        self.message = "OVS Port {%(interface)s} doesn't exist on OVS Bridge {%(bridge)s}, look for instance at Linux network configuration file {/etc/network/interfaces}" % locals()
     
    def __str__(self):
        return repr(self.message)
    
class RemotePEMACAddressNotFound(Exception):
    def __init__(self, ipAddress):
        self.message = "MAC address for remote router %(ipAddress)s could not be found. CAUTION: Must have direct MPLS connection" % locals()
     
    def __str__(self):
        return repr(self.message)
       