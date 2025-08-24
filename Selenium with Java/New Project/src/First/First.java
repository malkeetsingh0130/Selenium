package First;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class First {
	WebDriver driver;
	
	//launching firefox
	public void LaunchBrowser() throws InterruptedException {
		System.setProperty("webdriver.gecko.driver","D:/Projects/Installables/geckodriver.exe");
		driver = new FirefoxDriver();
		driver.navigate().to("https://www.simplilearn.com");
	}
	//searching for selenium course and clicking on it
	public void search() throws InterruptedException {
		driver.findElement(By.id("header_srch")).sendKeys("selenium");
		driver.findElement(By.xpath("/html/body/div[2]/div/div[1]/header/div/div/div/nav/div[3]/div[1]/form/button[3]/span")).click();
		Thread.sleep(3000);
		driver.findElement(By.xpath("//h4[text()='Automation Testing Masters Program']")).click();
		Thread.sleep(3000);
		System.out.println("The Page Title is- "+driver.getTitle());
	
	}
	//CLosing the Browser
	public void close() {
		driver.quit();
	}
	
	public static void main(String[] args) throws InterruptedException {
		First obj= new First();
		obj.LaunchBrowser();
		obj.search();
		obj.close();

	}

}
