package com.change_vision.jude.api.test.model;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

import junit.framework.Test;

import com.change_vision.jude.api.inf.model.IERAttribute;
import com.change_vision.jude.api.inf.model.IEREntity;
import com.change_vision.jude.api.inf.model.IERModel;
import com.change_vision.jude.api.inf.model.IERRelationship;
import com.change_vision.jude.api.inf.model.IERSchema;
import com.change_vision.jude.api.inf.model.INamedElement;

public class IERRelationshipTest extends ITestCase {
    private IERSchema schema = null;

    public static Test suite() {
        return suite("testModel/judeAPITest/ERAPITest.jude", IERRelationshipTest.class);
    }
    
    protected void setUp() {
        IERModel erModel = (IERModel)getElement(project.getOwnedElements(), "ER_Model");
        schema = erModel.getSchemata()[0];
    }
    
    public void testGetLogicalName(){
        //Identifying Relationship0
        IEREntity entity = getEntity(schema.getEntities(), "Entity1");
        IERAttribute attribute = getERAttribute(entity, "e1_Attribute2");
        IERRelationship relationship = attribute.getReferencedRelationship();
        assertEquals("Identifying Relationship0", relationship.getLogicalName());
    }
    
    public void testGetPhysicalName(){
        //Identifying Relationship0
        IEREntity entity = getEntity(schema.getEntities(), "Entity1");
        IERAttribute attribute = getERAttribute(entity, "e1_Attribute2");
        IERRelationship relationship = attribute.getReferencedRelationship();
        assertEquals("p_Identifying Relationship0", relationship.getPhysicalName());
    }
    
    public void testGetVerbPhraseParent(){
        //Identifying Relationship0
        IEREntity entity = getEntity(schema.getEntities(), "Entity1");
        IERAttribute attribute = getERAttribute(entity, "e1_Attribute2");
        IERRelationship relationship = attribute.getReferencedRelationship();
        assertEquals("verbP2C", relationship.getVerbPhraseParent());
    }
    
    public void testGetVerbPhraseChild(){
        //Identifying Relationship0
        IEREntity entity = getEntity(schema.getEntities(), "Entity1");
        IERAttribute attribute = getERAttribute(entity, "e1_Attribute2");
        IERRelationship relationship = attribute.getReferencedRelationship();
        assertEquals("verbC2P", relationship.getVerbPhraseChild());
    }
    
    public void testIsParentRequired_true(){
        //Identifying Relationship1
        IEREntity entity = getEntity(schema.getEntities(), "Entity2");
        IERAttribute attribute = getERAttribute(entity, "e1_Attribute2");
        IERRelationship relationship = attribute.getReferencedRelationship();
        assertTrue(relationship.isParentRequired());
    }
    
    public void testIsParentRequired_false(){
        //"Non-identifying Relationship0"
        IEREntity entity = getEntity(schema.getEntities(), "Entity3");
        IERAttribute attribute = getERAttribute(entity, "e3_Attribute2");
        IERRelationship relationship = attribute.getReferencedRelationship();
        assertFalse(relationship.isParentRequired());
    }
    
    public void testIsIdentifying_true(){
        //Identifying Relationship1
        IEREntity entity = getEntity(schema.getEntities(), "Entity2");
        IERAttribute attribute = getERAttribute(entity, "e1_Attribute2");
        IERRelationship relationship = attribute.getReferencedRelationship();
        assertTrue(relationship.isIdentifying());
    }
    
    public void testIsIdentifying_false(){
        //"Non-identifying Relationship0"
        IEREntity entity = getEntity(schema.getEntities(), "Entity3");
        IERAttribute attribute = getERAttribute(entity, "e3_Attribute2");
        IERRelationship relationship = attribute.getReferencedRelationship();
        assertFalse(relationship.isIdentifying());
    }
    
    public void testIsNonIdentifying_true(){
        //"Non-identifying Relationship0"
        IEREntity entity = getEntity(schema.getEntities(), "Entity3");
        IERAttribute attribute = getERAttribute(entity, "e3_Attribute2");
        IERRelationship relationship = attribute.getReferencedRelationship();
        assertTrue(relationship.isNonIdentifying());
    }
    
    public void testIsNonIdentifying_false(){
        //Identifying Relationship1
        IEREntity entity = getEntity(schema.getEntities(), "Entity2");
        IERAttribute attribute = getERAttribute(entity, "e1_Attribute2");
        IERRelationship relationship = attribute.getReferencedRelationship();
        assertFalse(relationship.isNonIdentifying());
    }
   
    public void testIsMultiToMulti_true(){
        //Multi2Multi Relationship0
        IEREntity entity = getEntity(schema.getEntities(), "Entity8");
        IERRelationship[] relationships = entity.getChildrenRelationships();
        assertTrue(relationships[0].isMultiToMulti());
    }
    
    public void testIsMultiToMulti_false(){
        //Identifying Relationship1
        IEREntity entity = getEntity(schema.getEntities(), "Entity2");
        IERAttribute attribute = getERAttribute(entity, "e1_Attribute2");
        IERRelationship relationship = attribute.getReferencedRelationship();
        assertFalse(relationship.isMultiToMulti());
    }
   
    public void testGetFKs(){
        //Identifying Relationship0
        IEREntity entity = getEntity(schema.getEntities(), "Entity1");
        IERAttribute attribute = getERAttribute(entity, "e1_Attribute2");
        IERRelationship relationship = attribute.getReferencedRelationship();
        assertEquals(1, relationship.getForeignKeys().length);
    }
    
    public void testGetChild(){
        //Identifying Relationship1
        IEREntity entity = getEntity(schema.getEntities(), "Entity2");
        IERAttribute attribute = getERAttribute(entity, "e1_Attribute2");
        IERRelationship relationship = attribute.getReferencedRelationship();
        assertEquals("Entity2", relationship.getChild().getLogicalName());
    }
    
    public void testGetParent(){
        //Identifying Relationship1
        IEREntity entity = getEntity(schema.getEntities(), "Entity2");
        IERAttribute attribute = getERAttribute(entity, "e1_Attribute2");
        IERRelationship relationship = attribute.getReferencedRelationship();
        assertEquals("Entity1", relationship.getParent().getLogicalName());
    }

    private IERAttribute getERAttribute(IEREntity entity, String attributeName){
        List attributes = new ArrayList();
        attributes.addAll(Arrays.asList(entity.getPrimaryKeys()));
        attributes.addAll(Arrays.asList(entity.getNonPrimaryKeys()));
        
        return getERAttribute(attributes, attributeName);
    }
    
    private IEREntity getEntity(IEREntity[] entities, String name){
        for(int i = 0; i < entities.length; i++) {
            if(name.equals(((IEREntity)entities[i]).getName())){
                return (IEREntity)entities[i];
            }
        }
        return null;
    }
    
    private IERAttribute getERAttribute(List attributes, String attributeName){
        for(Iterator iter = attributes.iterator(); iter.hasNext();){
            INamedElement attribute = (INamedElement) iter.next();
            if(attributeName.equals(attribute.getName())){
                return (IERAttribute)attribute;
            }
        }
        return null;
    }
}
