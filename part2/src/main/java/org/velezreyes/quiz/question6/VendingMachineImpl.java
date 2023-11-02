package org.velezreyes.quiz.question6;

import java.util.HashMap;
import java.util.Map;

public class VendingMachineImpl implements VendingMachine{

  private int numQuarters;
  private Map<String,Drink> drinks;

  private VendingMachineImpl(){
    numQuarters = 0;
    drinks = new HashMap<>();
    drinks.put("ScottCola", new DrinkImpl("ScottCola",true,3));
    drinks.put("KarenTea", new DrinkImpl("KarenTea",false,4));
  }

  public static VendingMachine getInstance() {
    return new VendingMachineImpl();
  }

  @Override
  public void insertQuarter() {
    numQuarters++;    
  }

  @Override
  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
    if(!drinks.containsKey(name)) throw new UnknownDrinkException();

    Drink drink = drinks.get(name);

    if(numQuarters < drink.getPrice()) throw new NotEnoughMoneyException();

    giveChange();

    return drink;        
  }

  private void giveChange(){
    //gives change
    numQuarters = 0;
  }
}
