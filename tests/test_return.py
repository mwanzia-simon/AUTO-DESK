def get_scan_results():
     moved_count = 15
     skipped_count = 3
     failed_count = 2
     return moved_count,skipped_count,failed_count
 
moved,skipped,failed = get_scan_results()

print(f"moved: {moved}")
print(f"skipped: {skipped}")
print(f"failed: {failed}")
 
     