package basicexperiments;

public class Experiment {
	
	public Experiment(String name, int weight, int rating)
	{
		this.Name = name;
		this.Weight = weight;
		this.Rating = rating;
	}
	
	public String Name;
	
	public int Weight;
	
	public int Rating;
	
	@Override
	public boolean equals(Object obj)
	{
		if (obj == this) return true;
		
		if (obj == null || obj.getClass() != this.getClass()) return false;
		
		Experiment expmnt = (Experiment) obj;
		
		return this.Weight == expmnt.Weight && this.Name.equals(expmnt.Name) && this.Rating == expmnt.Rating;
	}
	
	@Override
	public int hashCode()
	{
		int result = 17;
		
		result = 31 * result + this.Weight;
		result = 31 * result + this.Rating;
		result = 31 * result + this.Name.hashCode();
		
		return result;
	}
}