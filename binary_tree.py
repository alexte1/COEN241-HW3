from mininet.topo import Topo

class BinaryTreeTopo (Topo):
  "Binary Tree Topology Class"

  def __init__(self):
    "Create the binary tree topology"
    Topo.__init__(self)

    #Add hosts

    host1 = self.addHost('h1')
    host2 = self.addHost('h2')
    host3 = self.addHost('h3')
    host4 = self.addHost('h4')
    host5 = self.addHost('h5')
    host6 = self.addHost('h6')
    host7 = self.addHost('h7')
    host8 = self.addHost('h8')

    #Add switches
    switch1 = self.addSwitch('s1')
    switch2 = self.addSwitch('s2')
    switch3 = self.addSwitch('s3')
    switch4 = self.addSwitch('s4')
    switch5 = self.addSwitch('s5')
    switch6 = self.addSwitch('s6')
    switch7 = self.addSwitch('s7')

    #Add links
    self.addLink(switch1, switch2)
    self.addLink(switch3, switch2)
    self.addLink(host1, switch3)
    self.addLink(host2, switch3)

    self.addLink(switch4, switch2)
    self.addLink(host3, switch4)
    self.addLink(host4, switch4)

    self.addLink(switch5, switch1)
    self.addLink(switch6, switch5)
    self.addLink(host5, switch6)
    self.addLink(host6, switch6)

    self.addLink(switch7, switch5)
    self.addLink(host7, switch7)
    self.addLink(host8, switch7)

topos = {'binary_tree': (lambda: BinaryTreeTopo())}

