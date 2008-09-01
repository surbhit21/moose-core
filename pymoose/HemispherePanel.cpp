#ifndef _pymoose_HemispherePanel_cpp
#define _pymoose_HemispherePanel_cpp
#include "HemispherePanel.h"
using namespace pymoose;
const std::string HemispherePanel::className = "HemispherePanel";
HemispherePanel::HemispherePanel(Id id):Panel(id){}
HemispherePanel::HemispherePanel(std::string path):Panel(className, path){}
HemispherePanel::HemispherePanel(std::string name, Id parentId):Panel(className, name, parentId){}
HemispherePanel::HemispherePanel(std::string name, PyMooseBase& parent):Panel(className, name, parent){}
HemispherePanel::HemispherePanel(const HemispherePanel& src, std::string objectName, PyMooseBase& parent):Panel(src, objectName, parent){}
HemispherePanel::HemispherePanel(const HemispherePanel& src, std::string objectName, Id& parent):Panel(src, objectName, parent){}
HemispherePanel::HemispherePanel(const HemispherePanel& src, std::string path):Panel(src, path){}
HemispherePanel::HemispherePanel(const Id& src, std::string name, Id& parent):Panel(src, name, parent){}
HemispherePanel::~HemispherePanel(){}
const std::string& HemispherePanel::getType(){ return className; }
#endif
