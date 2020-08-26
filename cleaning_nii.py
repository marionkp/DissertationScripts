def removeNonPDFDirectories(dpath):
    '''Visit 'dpath', removing any subdirectory not containing any PDF
       file. Return True if 'dpath' is removed.
    '''
    import os
    if os.path.isdir(dpath):
        print 'Entering', dpath
        entries = [os.path.join(dpath, entry) for entry in os.listdir(dpath)]
        subdirs = filter(os.path.isdir, entries)
        print '    Subdirectories:', subdirs
        if all(map(removeNonPDFDirectories, subdirs)):
            print '    All subdirectories were removed.'
            files = filter(os.path.isfile, entries)
            pdf_files = [f for f in files if f.endswith('hipp_manseg_r.nii.gz') or f.endswith('hipp_manseg_l.nii.gz')]
            print '    PDF files:', pdf_files
            if not pdf_files:
                try:
                    for f in files:
                        os.unlink(f)
                        print '    Removed file', f
                    os.rmdir(dpath)
                    print '    Removed directory', dpath
                except OSError as e:
                    # An error occurred: assume directory is not empty.
                    print '    ERROR:', e
                    print '    Keeping directory', dpath
                    return False
                # Directory was removed: report to caller.
                return True
        # Directory must be kept: report to caller.
        print '    Keeping directory', dpath
        return False
    else:
        return False

removeNonPDFDirectories('structural_clean')
