package com.change_vision.jude.api.test.model;

import junit.framework.Test;

import com.change_vision.jude.api.inf.model.IERAttribute;
import com.change_vision.jude.api.inf.model.IEREntity;
import com.change_vision.jude.api.inf.model.IERModel;
import com.change_vision.jude.api.inf.model.IERSchema;
import com.change_vision.jude.api.inf.model.IERSubtypeRelationship;
import com.change_vision.jude.api.inf.model.INamedElement;

public class IERSubtypeRelationshipTest extends ITestCase {
    private IERSubtypeRelationship subtype0 = null;
    private IERSubtypeRelationship subtype2 = null;

    public static Test suite() {
        return suite("testModel/judeAPITest/ERAPITest.jude", IERSubtypeRelationshipTest.class);
    }
    
    protected void setUp() {
        IERModel erModel = (IERModel)getElement(project.getOwnedElements(), "ER_Model");
        IERSchema schema = erModel.getSchemata()[0];
        IEREntity entity5 = getEntity(schema.getEntities(), "Entity5");
        subtype0 = (IERSubtypeRelationship) entity5.getChildrenSubtypeRelationships()[0];

        IEREntity entity12 = getEntity(schema.getEntities(), "Entity11");
        subtype2 = (IERSubtypeRelationship) entity12.getChildrenSubtypeRelationships()[0];
    }

    private boolean contains(Object[] array, String targetName){       
        for(int i = 0; i < array.length; i++){
            INamedElement element = (INamedElement) array[i];
            if(targetName.equals(((IERAttribute)element).getName())){
                return true;
            }
        }
        return false;
    }

    public void testGetLogicalName() {
        assertEquals("Subtype0", subtype0.getLogicalName());
    }

    public void testGetPhysicalName() {
        assertEquals("p_Subtype0", subtype0.getPhysicalName());
    }

    public void testGetParent() {
        assertEquals("Entity5", subtype0.getParent().getName());
    }
    
    public void testGetChild() {
        assertEquals("Entity7", subtype0.getChild().getName());
    }
    
    public void testGetDiscriminatorAttribute(){
        assertEquals("Attribute0", subtype0.getDiscriminatorAttribute().getName());
    }
    
    public void testIsConclusive_true(){
        assertTrue(subtype0.isConclusive());
    }
    
    public void testIsConclusive_false(){
        assertFalse(subtype2.isConclusive());
    }
    
    public void testGetSubTypeFKs(){
        IERAttribute[] fks = subtype2.getForeignKeys();
        assertTrue(contains(fks, "Attribute0"));
        assertTrue(contains(fks, "Attribute1"));
    }
    
    private IEREntity getEntity(IEREntity[] entities, String name){
        for(int i = 0; i < entities.length; i++) {
            if(name.equals(((IEREntity)entities[i]).getName())){
                return (IEREntity)entities[i];
            }
        }
        return null;
    }
}
