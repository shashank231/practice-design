import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

public class ConfigManager {
    private final Map<String, String> settings = Collections.synchronizedMap(new HashMap<>());
    private final ScheduledExecutorService scheduler = Executors.newScheduledThreadPool(1);

    public ConfigManager() {
        // Initialize default settings
        settings.put("setting_a", "default_a");
        settings.put("setting_b", "default_b");
        settings.put("setting_c", "default_c");
    }

    /**
     * Returns the current configuration map.
     */
    public Map<String, String> getConfigs() {
        // Synchronized to provide thread-safe access
        synchronized (settings) {
            return new HashMap<>(settings);
        }
    }

    /**
     * Starts a background thread that updates the settings every 10 seconds.
     */
    public void startUpdatingConfigsRegularly() {
        scheduler.scheduleAtFixedRate(() -> {
            try {
                Map<String, String> updatedSettings = fetchUpdatedSettingsFromApi();
                synchronized (settings) {
                    settings.putAll(updatedSettings);
                }
            } catch (Exception e) {
                // Log or handle API fetch exceptions
                System.err.println("Error updating configs: " + e.getMessage());
            }
        }, 0, 10, TimeUnit.SECONDS);
    }

    /**
     * Fetches updated settings from the API. (Simulated for this example)
     */
    private Map<String, String> fetchUpdatedSettingsFromApi() {
        // Simulate API call with dummy data
        Map<String, String> updatedSettings = new HashMap<>();
        updatedSettings.put("setting_a", "updated_a_" + System.currentTimeMillis());
        updatedSettings.put("setting_b", "updated_b_" + System.currentTimeMillis());
        updatedSettings.put("setting_c", "updated_c_" + System.currentTimeMillis());
        return updatedSettings;
    }

    /**
     * Stops the scheduler gracefully.
     */
    public void stopUpdatingConfigs() {
        scheduler.shutdown();
        try {
            if (!scheduler.awaitTermination(5, TimeUnit.SECONDS)) {
                scheduler.shutdownNow();
            }
        } catch (InterruptedException e) {
            scheduler.shutdownNow();
        }
    }

    public static void main(String[] args) throws InterruptedException {
        ConfigManager configManager = new ConfigManager();

        // Start the regular update process
        configManager.startUpdatingConfigsRegularly();

        // Simulate fetching configs regularly
        for (int i = 0; i < 5; i++) {
            System.out.println("Configs: " + configManager.getConfigs());
            Thread.sleep(5000);
        }

        // Stop the background thread
        configManager.stopUpdatingConfigs();
    }
}
