package com.change_vision.jude.api.test.model;

import com.change_vision.jude.api.inf.model.IElement;
import com.change_vision.jude.api.inf.model.ITaggedValue;
import junit.framework.Test;

public class ITaggedValueTest extends ITestCase {
    
    public static Test suite() {
        return suite("testModel/judeAPITest/IElementTest.jude", ITaggedValueTest.class);
    }

    public void testGetKey() {
        IElement element = getElement(project.getOwnedElements(), "UseCase0");
        ITaggedValue[] taggedValues = element.getTaggedValues();
        assertEquals("uc.description.summary", taggedValues[0].getKey());
        assertEquals("uc.description.precondition", taggedValues[1].getKey());
        assertEquals("uc.description.postcondition", taggedValues[2].getKey());
    }

    public void testGetValue() {
        IElement element = getElement(project.getOwnedElements(), "UseCase0");
        ITaggedValue[] taggedValues = element.getTaggedValues();
        assertEquals("summary", taggedValues[0].getValue());
        assertEquals("pre-condition", taggedValues[1].getValue());
        assertEquals("post-condition1\npost-condition2", taggedValues[2].getValue());
    }
}
