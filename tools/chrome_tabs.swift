import Foundation
import ScriptingBridge

// Talks to ONE Chrome process by pid, so an automation Chrome with the same bundle id
// (agent-browser, another session's test harness) is never read or touched. AppleScript's
// `tell application "Google Chrome"` binds to whichever instance it finds first.
//
// usage: chrome_tabs <pid> list            → "<win#>\t<tab#>\t<url>" per tab
//        chrome_tabs <pid> close <url>...  → closes tabs whose URL equals one of the args
//
// Built on demand by tools/tab_intake.py; the binary is a cache, not a repo file.
let args = CommandLine.arguments
guard args.count >= 2, let pid = pid_t(args[1]) else { fputs("usage: chrome_tabs <pid> list|close <url>...\n", stderr); exit(64) }
guard let app = SBApplication(processIdentifier: pid) else { fputs("no app for pid \(pid)\n", stderr); exit(2) }
app.timeout = 600
guard let windows = app.value(forKey: "windows") as? SBElementArray else { fputs("no windows\n", stderr); exit(3) }
let mode = args.count > 2 ? args[2] : "list"
let targets = Set(args.dropFirst(3))
for (wi, w) in windows.enumerated() {
    guard let w = w as? SBObject, let tabs = w.value(forKey: "tabs") as? SBElementArray else { continue }
    for i in stride(from: tabs.count - 1, through: 0, by: -1) {   // descending: closing keeps earlier indices valid
        guard let t = tabs.object(at: i) as? SBObject else { continue }
        let u = (t.value(forKey: "URL") as? String) ?? ""
        if mode == "list" { print("\(wi + 1)\t\(i + 1)\t\(u)") }
        else if mode == "close" && targets.contains(u) {
            t.perform(NSSelectorFromString("close"))
            print("closed \(u)")
        }
    }
}
