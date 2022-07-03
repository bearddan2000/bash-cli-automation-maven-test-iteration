package example;

import net.serenitybdd.core.Serenity;
import net.serenitybdd.core.steps.UIInteractionSteps;
import net.serenitybdd.junit5.SerenityJUnit5Extension;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;

import static org.assertj.core.api.Assertions.assertThat;

@ExtendWith(SerenityJUnit5Extension.class)
public class MainTest {

    @Test
    public void getGreeting() {
        String test = Main.greeting();
        String expected = "Hello World";
        Serenity.reportThat("First test",
                () -> assertThat(test).isEqualTo(expected)
        );
    }

}
