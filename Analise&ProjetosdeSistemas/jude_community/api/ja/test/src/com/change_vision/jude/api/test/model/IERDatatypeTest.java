package com.change_vision.jude.api.test.model;

import junit.framework.Test;

import com.change_vision.jude.api.inf.model.IERDatatype;
import com.change_vision.jude.api.inf.model.IERModel;
import com.change_vision.jude.api.inf.model.IERSchema;

public class IERDatatypeTest extends ITestCase {
    private IERSchema schema;

    public static Test suite() {
        return suite("testModel/judeAPITest/ERAPITest.jude", IERDatatypeTest.class);
    }
    
    protected void setUp() {
        IERModel erModel = (IERModel)getElement(project.getOwnedElements(), "ER_Model");
        schema = erModel.getSchemata()[0];
    }
    
    public void testGetLengthConstraint() {
        IERDatatype datatype = getDatatype(schema.getDatatypes(), "BIT");
        assertEquals("Required", datatype.getLengthConstraint());
    }
    
    public void testGetPrecisionConstraint() {
        IERDatatype datatype = getDatatype(schema.getDatatypes(), "BIT");
        assertEquals("None", datatype.getPrecisionConstraint());
    }
    
    public void testGetDefaultLengthPrecision() {
        IERDatatype datatype = getDatatype(schema.getDatatypes(), "NUMERIC");
        assertEquals("10,5", datatype.getDefaultLengthPrecision());
    }
    
    public void testGetDescription() {
        IERDatatype datatype = getDatatype(schema.getDatatypes(), "NUMERIC");
        assertEquals("desc", datatype.getDescription());
    }
    
    private IERDatatype getDatatype(IERDatatype[] datatypes, String name){
        for(int i = 0; i < datatypes.length; i++) {
            if(name.equals(((IERDatatype)datatypes[i]).getName())){
                return (IERDatatype)datatypes[i];
            }
        }
        return null;
    }
    
//    public void testGetTypeInv() {
//        IERDatatype datatype = (IERDatatype)getElement(dtModel.getOwnedElements(), "DATE");
//        IERAttribute[] typeInv = datatype.getTypeInv();
//        assertTrue(contains(typeInv, "Attribute0"));
//        assertTrue(contains(typeInv, "Attribute4"));
//    }
//    
//    private boolean contains(Object[] array, String targetName){       
//        for(int i = 0; i < array.length; i++){
//            INamedElement element = (INamedElement) array[i];
//            if(targetName.equals(element.getName())){
//                return true;
//            }
//        }
//        return false;
//    }
}