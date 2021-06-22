package com.change_vision.jude.api.test.model;

import junit.framework.Test;
import JP.co.esm.caddies.er.simpleER.SimpleEREntity;

import com.change_vision.jude.api.inf.model.IEREntity;
import com.change_vision.jude.api.inf.model.IERModel;
import com.change_vision.jude.api.inf.model.IERSchema;

public class IEREntityTest extends ITestCase {
    private IERSchema schema = null;

    public static Test suite() {
        return suite("testModel/judeAPITest/ERAPITest.jude", IEREntityTest.class);
    }
    
    protected void setUp() {
        IERModel erModel = (IERModel)getElement(project.getOwnedElements(), "ER_Model");
        schema = erModel.getSchemata()[0];
    }
    
    public void testGetLogicalName() {
        IEREntity entity = getEntity(schema.getEntities(), "Entity4");
        assertEquals("Entity4", entity.getLogicalName());
    }

    public void testGetPhysicalName() {
        IEREntity entity = getEntity(schema.getEntities(), "Entity4");
        assertEquals("p_Entity4", entity.getPhysicalName());
    }

    public void testGetType() {
        IEREntity entity = getEntity(schema.getEntities(), "Entity4");
        assertEquals(SimpleEREntity.TYPE_SUMMARY, entity.getType());
    }
    
    public void testGetPrimaryKeys() {
        IEREntity entity = getEntity(schema.getEntities(), "Entity4");
        assertEquals(3, entity.getPrimaryKeys().length);
    }
    
    public void testGetForeignKeys() {
        IEREntity entity = getEntity(schema.getEntities(), "Entity7");
        assertEquals(2, entity.getForeignKeys().length);
    }
    
    public void testGetNonPrimaryKeys() {
        IEREntity entity = getEntity(schema.getEntities(), "Entity7");
        assertEquals(2, entity.getNonPrimaryKeys().length);
    }
    
    public void testGetChildrenRelationships() {
        IEREntity entity = getEntity(schema.getEntities(), "Entity1");
        assertEquals(1, entity.getChildrenRelationships().length);
    }
    
    public void testGetParentRelationships() {
        IEREntity entity = getEntity(schema.getEntities(), "Entity16");
        assertEquals(2, entity.getParentRelationships().length);
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
