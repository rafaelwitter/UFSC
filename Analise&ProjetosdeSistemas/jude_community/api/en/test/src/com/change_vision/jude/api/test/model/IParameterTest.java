package com.change_vision.jude.api.test.model;

import com.change_vision.jude.api.inf.model.IClass;
import com.change_vision.jude.api.inf.model.IOperation;
import com.change_vision.jude.api.inf.model.IParameter;
import junit.framework.Test;

public class IParameterTest extends ITestCase {

    public static Test suite() {
        return suite("testModel/judeAPITest/IOperationTest.jude", IParameterTest.class);
    }

    public void testGetType_Class1_ARRAY() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IOperation op = (IOperation)getElement(cls.getOperations(), "operation3");
        IParameter param = (IParameter)getElement(op.getParameters(), "param0");
        assertEquals("Class1", param.getType().getName());
        assertEquals("Class1[]", param.getTypeExpression());
	}

    public void testGetType_int() {
        IClass cls = (IClass)getElement(project.getOwnedElements(), "Class0");
        IOperation op = (IOperation)getElement(cls.getOperations(), "operation3");
        IParameter param = (IParameter)getElement(op.getParameters(), "param1");
        assertEquals("int", param.getType().getName());
        assertEquals("int", param.getTypeExpression());
    }
}
