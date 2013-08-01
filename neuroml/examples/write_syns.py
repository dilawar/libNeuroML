"""

Example to create a file with multiple synapse types

"""

from neuroml import NeuroMLDocument
from neuroml import *
import neuroml.writers as writers
from random import random


nml_doc = NeuroMLDocument(id="SomeSynapses")

expOneSyn0 = ExpOneSynapse(id="ampa", tau_decay="5ms", gbase="1nS", erev="0mV")
nml_doc.exp_one_synapses.append(expOneSyn0)

expTwoSyn0 = ExpTwoSynapse(id="gaba", tau_decay="12ms", tau_rise="3ms", gbase="1nS", erev="-70mV")
nml_doc.exp_two_synapses.append(expTwoSyn0)

bpSyn = BlockingPlasticSynapse(id="blockStpSynDep", gbase="1nS", erev="0mV", tau_rise="0.1ms", tau_decay="2ms")
bpSyn.notes = "This is a note"
bpSyn.plasticity_mechanism = PlasticityMechanism(type="tsodyksMarkramDepMechanism", init_release_prob="0.5", tau_rec="120 ms")
bpSyn.block_mechanism = BlockMechanism(type="voltageConcDepBlockMechanism", species="mg", block_concentration="1.2 mM", scaling_conc="1.920544 mM", scaling_volt="16.129 mV")

nml_doc.blocking_plastic_synapses.append(bpSyn)


newnmlfile = 'tmp/synapses.xml'
writers.NeuroMLWriter.write(nml_doc, newnmlfile)
print("Saved to: "+newnmlfile)


from lxml import etree
from urllib import urlopen
schema_file = urlopen("https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta.xsd")
xmlschema = etree.XMLSchema(etree.parse(schema_file))
print "Validating %s against %s" %(newnmlfile, schema_file.geturl())
xmlschema.assertValid(etree.parse(newnmlfile))
print "It's valid!"

