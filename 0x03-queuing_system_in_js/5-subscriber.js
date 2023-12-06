/**
 * Redis subscriber cient
 */
import { createClient, print } from 'redis';

// Create a redis client
const sub = createClient();
sub.on('error', (err) => console.log('Redis client not connected to the server:', err));
sub.on('connect', () => console.log('Redis client connected to the server'));

// Subscribe to holberton school channel
const channel = 'holberton school channel'
sub.subscribe(channel);

// Log message when received
sub.on('message', (channel, message) => {
    console.log(message);
    if (message === 'KILL_SERVER') {
        sub.unsubscribe();
        sub.quit();
    }
})