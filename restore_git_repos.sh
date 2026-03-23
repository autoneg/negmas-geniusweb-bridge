
# Repository: projects/negmas-geniusweb-bridge
echo -e "${BLUE}Restoring: projects/negmas-geniusweb-bridge${NC}"
if [ -d "projects/negmas-geniusweb-bridge/.git" ]; then
    echo -e "  ${YELLOW}Directory already exists, skipping...${NC}"
else
    # Create parent directory if needed
    mkdir -p "projects"
    
    # Clone the repository
    if git clone "git@github.com:autoneg/negmas-geniusweb-bridge.git" "projects/negmas-geniusweb-bridge"; then
        echo -e "  ${GREEN}✓${NC} Successfully cloned"
        
        # Checkout the original branch if not already on it
        cd "projects/negmas-geniusweb-bridge"
        current=$(git rev-parse --abbrev-ref HEAD)
        if [ "$current" != "main" ]; then
            if git checkout "main" 2>/dev/null; then
                echo -e "  ${GREEN}✓${NC} Checked out branch: main"
            else
                echo -e "  ${YELLOW}⚠${NC} Could not checkout branch: main"
            fi
        fi
        cd - > /dev/null
    else
        echo -e "  ${RED}✗${NC} Failed to clone"
    fi
fi


# Repository: projects/negmas-geniusweb-bridge
echo -e "${BLUE}Restoring: projects/negmas-geniusweb-bridge${NC}"
if [ -d "projects/negmas-geniusweb-bridge/.git" ]; then
    echo -e "  ${YELLOW}Directory already exists, skipping...${NC}"
else
    # Create parent directory if needed
    mkdir -p "projects"
    
    # Clone the repository
    if git clone "git@github.com:autoneg/negmas-geniusweb-bridge.git" "projects/negmas-geniusweb-bridge"; then
        echo -e "  ${GREEN}✓${NC} Successfully cloned"
        
        # Checkout the original branch if not already on it
        cd "projects/negmas-geniusweb-bridge"
        current=$(git rev-parse --abbrev-ref HEAD)
        if [ "$current" != "main" ]; then
            if git checkout "main" 2>/dev/null; then
                echo -e "  ${GREEN}✓${NC} Checked out branch: main"
            else
                echo -e "  ${YELLOW}⚠${NC} Could not checkout branch: main"
            fi
        fi
        cd - > /dev/null
    else
        echo -e "  ${RED}✗${NC} Failed to clone"
    fi
fi


# Repository: projects/negmas-geniusweb-bridge
echo -e "${BLUE}Restoring: projects/negmas-geniusweb-bridge${NC}"
if [ -d "projects/negmas-geniusweb-bridge/.git" ]; then
    echo -e "  ${YELLOW}Directory already exists, skipping...${NC}"
else
    # Create parent directory if needed
    mkdir -p "projects"
    
    # Clone the repository
    if git clone "git@github.com:autoneg/negmas-geniusweb-bridge.git" "projects/negmas-geniusweb-bridge"; then
        echo -e "  ${GREEN}✓${NC} Successfully cloned"
        
        # Checkout the original branch if not already on it
        cd "projects/negmas-geniusweb-bridge"
        current=$(git rev-parse --abbrev-ref HEAD)
        if [ "$current" != "main" ]; then
            if git checkout "main" 2>/dev/null; then
                echo -e "  ${GREEN}✓${NC} Checked out branch: main"
            else
                echo -e "  ${YELLOW}⚠${NC} Could not checkout branch: main"
            fi
        fi
        cd - > /dev/null
    else
        echo -e "  ${RED}✗${NC} Failed to clone"
    fi
fi

